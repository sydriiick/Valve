from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (StationFive, StationFour, StationOne, Stationsix,
                     StationTwo)
from .serializers import *

class StationOneView(generics.GenericAPIView):
    serializer_class = StationOneSerializer
    def post(self, request): 
        serializer = StationOneSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        return Response(serializer.errors)

class StationTwoView(generics.GenericAPIView):
    serializer_class = StationTwoSerializer
    def post(self, request): 
        serializer = StationTwoSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        return Response(serializer.errors)

class StationFourView(generics.GenericAPIView):
    serializer_class = StationFourSerializer
    def post(self, request): 
        serializer = StationFourSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        return Response(serializer.errors)

class StationFiveView(generics.GenericAPIView):
    serializer_class = StationFiveSerializer
    def post(self, request): 
        serializer = StationFiveSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        return Response(serializer.errors)

class StationSixView(generics.GenericAPIView):
    serializer_class = StationSixSerializer
    def post(self, request): 
        serializer = StationSixSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return Response(status=status.HTTP_201_CREATED) 
        return Response(serializer.errors)