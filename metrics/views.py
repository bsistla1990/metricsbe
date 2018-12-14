from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from pm.models import Teams
from pm.models import Tracks
from pm.models import Users
from django.contrib.auth.models import User


@api_view(['GET'])
def getUser(request):
    if request.GET.get('userName') is not None:
        try:
            user1 = User.objects.get(username = request.GET['userName'])
            glist =[]
            groups = user1.groups.all()
            for group in groups:
                glist.append(group.name)
            cuser = Users.objects.filter(user__id = user1.pk).first()
            result  = {'team': cuser.team.team, 'track': cuser.track.track, 'userName': cuser.user.username, \
             'email': cuser.user.email, 'super_user': cuser.user.is_superuser, \
             'staff': cuser.user.is_staff, 'active': cuser.user.is_active, 'groups':glist}
            if cuser is not None:
                return Response(json.dumps(result))
        except Exception as ex:
            print(dir(ex.__str__()))
            return Response(json.dumps({'status':'failed', 'data':ex.__str__()}))
    elif request.GET.get('track') is not None:
        ulist = []
        users = Users.objects.filter(track__track = request.GET['track'])
        for user in users:
            ulist.append({'user': user.user.username})
        return Response(json.dumps(ulist))
    else:
        users = Users.objects.all()
        ulist = [];
        for usr in users:
            ulist.append(
                {'team': usr.team.team, 'track': usr.track.track, 'userName': usr.user.username, \
                            'email': usr.user.email, 'super_user': usr.user.is_superuser, \
                            'staff': usr.user.is_staff, 'active': usr.user.is_active})
        return Response(json.dumps(ulist))

@api_view(['GET'])
def getTeams(request):
    teams = Teams.objects.all()
    tlist = []
    for team in teams:
        tlist.append({
            'team': team.team
        })
    return Response(json.dumps(tlist))

@api_view(['GET'])
def getTracks(request):
    tlist = []
    if request.GET.get('team') is not None:
        try:
            team = Teams.objects.get(team=request.GET['team'])

            ctrack = Tracks.objects.filter(team__team=team.team).all()
            for t in ctrack:
                tlist.append({'team': t.team.team, 'track': t.track})
            if ctrack is not None:
                return Response(json.dumps(tlist))
        except Exception as ex:
            print(dir(ex.__str__()))
            return Response(json.dumps({'status': 'failed', 'data': ex.__str__()}))
    elif request.GET.get('track') is not None:
        try:
            ctrack = Tracks.objects.filter(track=request.GET['track']).all()
            for t in ctrack:
                tlist.append({'team': t.team.team, 'track': t.track})
            if ctrack is not None:
                return Response(json.dumps(tlist))
        except Exception as ex:
            print(dir(ex.__str__()))
            return Response(json.dumps({'status': 'failed', 'data': ex.__str__()}))
    else:
        tracks = Tracks.objects.all()

        for track in tracks:
            tlist.append(json.dumps({
                'team': track.team.team,
                'track':track.track
            }))
        return Response(tlist)