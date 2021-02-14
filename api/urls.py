from django.urls import path
from . import views

urlpatterns = [
    path('station-one/', views.StationOneView.as_view(), name='station-one'),
    path('station-two/', views.StationTwoView.as_view(), name='station-two'),
    path('station-four/', views.StationFourView.as_view(), name='station-four'),
    path('station-five/', views.StationFiveView.as_view(), name='station-five'),
    path('station-six/', views.StationSixView.as_view(), name='station-six'),
]
