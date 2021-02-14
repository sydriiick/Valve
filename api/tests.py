from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import serializers, status
# Create your tests here.

class StationOneTestCase(APITestCase):
    def test_station_one(self):
        data = {
                "unique": "1",
                "data_1": 2.2,
                "data_2": 2.2,
                "data_3": 2.2,
                }
        url = reverse('station-one')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_station_two(self):
        data = {
                "unique": "2",
                "data": 2.2,
                }
        url = reverse('station-two')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)   

    def test_station_four(self):
        data = {
                "unique": "2",
                "data": 2.2,
                }
        url = reverse('station-four')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)  

    def test_station_five(self):
        data = {
                "unique": "2",
                "data": 2.2,
                }
        url = reverse('station-five')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)  

    def test_station_six(self):
        data = {
                "unique": "2",
                "data": 2.2,
                }
        url = reverse('station-six')
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)                           