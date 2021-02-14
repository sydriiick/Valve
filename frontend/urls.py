from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('one/', views.one_data, name='one_data'),
    path('two/', views.two_data, name='two_data'),
    path('four/', views.four_data, name='four_data'),
    path('five/', views.five_data, name='five_data'),
    path('six/', views.six_data, name='six_data'),
]
