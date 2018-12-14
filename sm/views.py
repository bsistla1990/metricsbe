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

from sm.models import Sprint
from sm.models import UpsDowns

from django.contrib.auth.models import User

@api_view(['POST'])
def addSprint(request):
    user = Users.objects.filter(user__username = request.data['user']).first()
    team = Teams.objects.filter(team = request.data['team']).first()
    track = Tracks.objects.filter(track = request.data['track']).first()
    body = request.data
    if user is not None:
        for d in body['stories']:
            spsummary = Sprint(team = team, track = track, user = user, sprint = body['sprint'], \
                         startDate = body['startDate'], endDate = body['endDate'], activity = d['activity'],\
                        story = d['story'], points= d['points'])
            spsummary.save()
    return Response(json.dumps({'status':'success', 'message':'Sprint summary saved successfully'}))

@api_view(['GET'])
def index(request):
    slist=[]
    ssummary = Sprint.objects.filter(user__user__username = request.GET['userName']).order_by('-id')[:15]
    for s in ssummary:
        slist.append({'id': s.pk, 'team': s.team.team, 'track':s.track.track, 'user':s.user.user.username,\
                      'sprint': s.sprint, 'startDate':str(s.startDate), 'endDate': str(s.endDate),'activity':s.activity,\
                      'story':s.story, 'points':s.points})
    return Response(json.dumps(slist))

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

    slist = []
    ssummary = Sprint.objects.filter(**vals).all()
    for s in ssummary:
        slist.append({'id': s.pk, 'team': s.team.team, 'track':s.track.track, 'user':s.user.user.username,\
                      'sprint': s.sprint, 'startDate':str(s.startDate), 'endDate': str(s.endDate),\
                      'activity':s.activity, 'story':s.story, 'points':s.points})
    return Response(json.dumps(slist))

@api_view(['POST'])
def delete(request):
    ssummary = Sprint.objects.filter(pk=request.data['id'])
    if ssummary is not None:
        ssummary.delete()
        return Response(json.dumps({'status': 'success', 'message': 'Record deleted succesfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Record to delete not found'}))

@api_view(['POST'])
def update(request):
    body = request.data
    ssummary = Sprint.objects.filter(pk= body['id']).first()
    if ssummary is not None:
        ssummary.sprint = body['sprint']
        ssummary.startDate = body['startDate']
        ssummary.endDate = body['endDate']
        ssummary.activity = body['activity']
        ssummary.story = body['story']
        ssummary.points = body['points']

        ssummary.save()
        return Response(json.dumps({'status':'success', 'message':'Metrics updated successfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Metrics failed to update'}))


###################################################### Ups and Downs ###################################################
@api_view(['POST'])
def addUpDown(request):
    team = Teams.objects.filter(team = request.data['team']).first()
    track = Tracks.objects.filter(track = request.data['track']).first()
    body = request.data
    for d in body['uds']:
        ud = UpsDowns(team = team, track = track, sprint = body['sprint'], \
                     startDate = body['startDate'], endDate = body['endDate'], type = d['type'],\
                      val = d['val'])
        ud.save()
    return Response(json.dumps({'status':'success', 'message':'Ups and Downs summary saved successfully'}))

@api_view(['GET'])
def ud_index(request):
    udlist=[]
    udsummary = UpsDowns.objects.filter(track__track = request.GET['track']).order_by('-id')[:15]
    for s in udsummary:
        udlist.append({'id': s.pk, 'team': s.team.team, 'track':s.track.track, \
                      'sprint': s.sprint, 'startDate':str(s.startDate), 'endDate': str(s.endDate),\
                      'type':s.type, 'val':s.val})
    return Response(json.dumps(udlist))

@api_view(['POST'])
def ud_search(request):
    body = request.data
    vals = {}
    if 'team' in body and body['team']:
        vals['team__team']=  body['team']
    if 'track' in body and body['track']:
        vals['track__track'] = body['track']
    if 'sprint' in body and body['sprint']:
        vals['sprint'] =int(body['sprint'])
    if 'type' in body and body['type']:
        vals['type'] = body['type']

    udlist = []
    udsummary = UpsDowns.objects.filter(**vals).all()
    for s in udsummary:
        udlist.append({'id': s.pk, 'team': s.team.team, 'track':s.track.track, \
                      'sprint': s.sprint, 'startDate':str(s.startDate), 'endDate': str(s.endDate),\
                      'type':s.type, 'val':s.val})
    return Response(json.dumps(udlist))

@api_view(['POST'])
def ud_delete(request):
    ud = UpsDowns.objects.filter(pk=request.data['id'])
    if ud is not None:
        ud.delete()
        return Response(json.dumps({'status': 'success', 'message': 'Record deleted succesfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Record to delete not found'}))

@api_view(['POST'])
def ud_update(request):
    body = request.data
    ud = UpsDowns.objects.filter(pk= body['id']).first()
    if ud is not None:
        ud.type = body['type']
        ud.val = body['val']

        ud.save()
        return Response(json.dumps({'status':'success', 'message':'Metrics updated successfully'}))
    return Response(json.dumps({'status': 'failed', 'message': 'Metrics failed to update'}))