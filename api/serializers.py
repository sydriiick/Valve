from rest_framework import serializers
from datetime import datetime
from django.utils import timezone
from .models import StationOne, StationTwo, StationFour, StationFive, Stationsix


class StationOneSerializer(serializers.ModelSerializer):  # user info serializer
    class Meta:
        model = StationOne
        fields = '__all__'
    def create(self, validated_data):   
        valve = StationOne.objects.create(**validated_data)
        valve.unique = validated_data['unique']+ ','+ str(timezone.now().date())
        valve.save()
        return valve

class StationTwoSerializer(serializers.ModelSerializer):  # user info serializer
    class Meta:
        model = StationTwo
        fields = '__all__'
    def create(self, validated_data):   
        valve = StationTwo.objects.create(**validated_data)
        valve.unique = validated_data['unique']+ ','+ str(timezone.now().date())
        valve.save()
        return valve

class StationFourSerializer(serializers.ModelSerializer):  # user info serializer
    class Meta:
        model = StationFour
        fields = '__all__'
    def create(self, validated_data):   
        valve = StationFour.objects.create(**validated_data)
        valve.unique = validated_data['unique']+ ','+ str(timezone.now().date())
        valve.save()
        return valve

class StationFiveSerializer(serializers.ModelSerializer):  # user info serializer
    class Meta:
        model = StationFive
        fields = '__all__'
    def create(self, validated_data):   
        valve = StationFive.objects.create(**validated_data)
        valve.unique = validated_data['unique']+ ','+ str(timezone.now().date())
        valve.save()
        return valve

class StationSixSerializer(serializers.ModelSerializer):  # user info serializer
    class Meta:
        model = Stationsix
        fields = '__all__'
    def create(self, validated_data):   
        valve = Stationsix.objects.create(**validated_data)
        valve.unique = validated_data['unique']+ ','+ str(timezone.now().date())
        valve.save()
        return valve