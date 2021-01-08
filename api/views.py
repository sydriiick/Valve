from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated

from .models  import *
from .serializers import ShutdownValveSerializers
from django.utils import timezone

@api_view(['GET'])
def valveList(request):
    valve = ShutdownValve.objects.all()
    serializer = ShutdownValveSerializers(valve, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def valveDetail(request, pk):
    valve = ShutdownValve.objects.get(id=pk)
    serializer = ShutdownValveSerializers(valve, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def valveCreate(request):
    serializer = ShutdownValveSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def valveUpdate(request, pk):

    val = request.data.get('valve')

    try:
        valve = ShutdownValve.objects.get(id=pk)
    except Route.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if valve.station_five == None and valve.station_six == None:
        valve.station_five = val
        valve.save()
        return Response("success",status=status.HTTP_202_ACCEPTED)
    elif valve.station_five != None and valve.station_six == None:
        valve.station_six = val
        valve.save()
        return Response("success",status=status.HTTP_202_ACCEPTED)
    else:
        return Response("not sucess",status=status.HTTP_400_BAD_REQUEST)
