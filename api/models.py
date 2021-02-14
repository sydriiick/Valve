from django.db import models
from datetime import datetime

class StationOne(models.Model):
    unique = models.CharField(max_length=30)
    data_1 = models.FloatField(default=0)
    data_2 = models.FloatField(default=0)
    data_3 = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unique

class StationTwo(models.Model):
    unique = models.CharField(max_length=30)
    data = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.data)

class StationFour(models.Model):
    unique = models.CharField(max_length=30)
    data = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.data)

class StationFive(models.Model):
    unique = models.CharField(max_length=30)
    data = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.data)

class Stationsix(models.Model):
    unique = models.CharField(max_length=30)
    data = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.data)

class Default(models.Model):
    station = models.CharField(max_length=10)
    minimum = models.FloatField(default=0)
    maximum = models.FloatField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.station)
