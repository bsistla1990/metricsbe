from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pm.models import Metrics
from rest_framework.decorators import api_view
import json

import datetime

from pm.models import Metrics
from pm.models import Teams
from pm.models import Tracks
from pm.models import Users
from django.contrib.auth.models import User

@api_view(['POST'])
def addProductivity(request):
    user = Users.objects.filter(user__username = request.data['user']).first()
    team = Teams.objects.filter(team = request.data['team']).first()
    track = Tracks.objects.filter(track = request.data['track']).first()
    body = request.data
    if user is not None:
        metric = Metrics(team = team, track = track, user = user, sprint = body['sprint'], \
                         startDate = body['startDate'], endDate = body['endDate'], devStories = body['devStories'], \
                         devStoryPoints = body['devPoints'], devCommits = body['devCommits'], qaStories = body['qaStories'], \
                         qaStoryPoints = body['qaPoints'], qaCommits = body['qaCommits'])
        metric.save()
        metrics = Metrics.objects.filter(pk=metric.pk).first()
    return Response(json.dumps({'team': metrics.team.team, 'track': metrics.track.track, 'user':metrics.user.user.username,\
                                'sprint': metrics.sprint, 'devStories':metrics.devStories, 'devPoints': metrics.devStoryPoints,\
                                'devCommits':metrics.devCommits, 'qaStories':metrics.qaStories, 'qaPoints': metrics.qaStoryPoints,\
                                'qaCommits':metrics.qaCommits}))

@api_view(['GET'])
def index(request):
    mlist=[]
    metrics = Metrics.objects.filter(user__user__username = request.GET['userName']).order_by('-id')[:15]
    for metric in metrics:
        mlist.append({'id': metric.pk, 'team': metric.team.team, 'track':metric.track.track, 'user':metric.user.user.username,\
                      'sprint': metric.sprint, 'devStories': metric.devStories, 'devPoints': metric.devStoryPoints,\
                      'devCommits': metric.devCommits, 'qaStories': metric.qaStories, 'qaPoints': metric.qaStoryPoints,\
                      'qaCommits': metric.qaCommits, 'startDate': str(metric.startDate), 'endDate':str(metric.endDate)})
    return Response(json.dumps(mlist))

@api_view(['POST'])
def search(request):
    body = request.data
    vals = {}
    if 'team' in body and body['team']:
        vals['team__team']=  body['team']
    if 'track' in body and body['track']:
        vals['track__track'] = body['track']
    if 'user' in body and body['user']:
        vals['user__user__username'] = body['user']
    if 'sprint' in body and body['sprint']:
        vals['sprint'] =body['sprint']
    if 'startDate' in body and body['startDate']:
        endDate = ''
        if 'endDate' in body and body['endDate']:
            endDate = body['endDate']
        else:
            endDate =  datetime.datetime.today().strftime('%Y-%m-%d')
        vals['startDate__range']=(body['startDate'], endDate)

    mlist = []
    metrics = Metrics.objects.filter(**vals).all()
    for metric in metrics:
        mlist.append({'id':metric.pk, 'team': metric.team.team, 'track':metric.track.track, 'user':metric.user.user.username,\
                      'sprint': metric.sprint, 'devStories': metric.devStories, 'devPoints': metric.devStoryPoints,\
                      'devCommits': metric.devCommits, 'qaStories': metric.qaStories, 'qaPoints': metric.qaStoryPoints,\
                      'qaCommits': metric.qaCommits, 'startDate': str(metric.startDate), 'endDate':str(metric.endDate)})
    return Response(json.dumps(mlist))

@api_view(['POST'])
def delete(request):
    metric = Metrics.objects.filter(pk=request.data['id'])
    if metric is not None:
        metric.delete()
        return Response(json.dumps({'status': 'success', 'message': 'Record deleted succesfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Record to delete not found'}))

@api_view(['POST'])
def update(request):
    body = request.data
    metric = Metrics.objects.filter(pk= body['id']).first()
    if metric is not None:
        metric.sprint = body['sprint']
        metric.startDate = body['startDate']
        metric.endDate = body['endDate']
        metric.devStoryPoints = body['devPoints']
        metric.qaStoryPoints = body['qaPoints']
        metric.devCommits = body['devCommits']
        metric.qaCommits = body['qaCommits']
        metric.devStories = body['devStories']
        metric.qaStories = body['qaStories']

        metric.save()
        return Response(json.dumps({'status':'success', 'message':'Metrics updated successfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Metrics failed to update'}))