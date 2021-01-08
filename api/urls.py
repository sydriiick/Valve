from django.urls import path
from . import views

urlpatterns = [
    path('valve-list', views.valveList, name='valve-list'),
    path('valve-detail/<str:pk>', views.valveDetail, name='valve-detail'),
    path('valve-create', views.valveCreate, name='valve-create'),
    path('valve-update/<str:pk>', views.valveUpdate, name='valve-update'),
]
