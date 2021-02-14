from api.models import (StationFive, StationFour, StationOne, Stationsix,
                        StationTwo, Default)
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect, get_object_or_404
from django import template



def home(request):
    if request.POST:
        station = request.POST.get('station')
        minimum = request.POST.get('minimum')
        maximum = request.POST.get('maximum')
        default = get_object_or_404(Default, station=station)
        default.minimum = float(minimum)
        default.maximum = float(maximum)
        default.save()
        return redirect('home')
        
    one_list = StationOne.objects.order_by('-date_created')
    two_list = StationTwo.objects.order_by('-date_created')
    four_list = StationFour.objects.order_by('-date_created')
    five_list = StationFive.objects.order_by('-date_created')
    six_list = Stationsix.objects.order_by('-date_created')

    
    s1 = Default.objects.get(station="Station 1")
    s2 = Default.objects.get(station="Station 2")
    s4 = Default.objects.get(station="Station 4")
    s5 = Default.objects.get(station="Station 5")
    s6 = Default.objects.get(station="Station 6")
    context = {
        'one_list': one_list,
        'two_list': two_list,
        'four_list': four_list,
        'five_list': five_list,
        'six_list': six_list,
        
        's1': s1,
        's2': s2,
        's4': s4,
        's5': s5,
        's6': s6,
        }
    return render(request, 'home.html', context)
    

def one_data(request):
    s1 = Default.objects.get(station="Station 1")
    one_list = StationOne.objects.order_by('-date_created')
    context = {
        'one_list': one_list,
        's1': s1,
        }
    return render(request, 'one_data.html', context)

def two_data(request):
    two_list = StationTwo.objects.order_by('-date_created')
    s2 = Default.objects.get(station="Station 2")
    context = {
        'two_list': two_list,
        's2': s2,
        }
    return render(request, 'two_data.html', context)

def four_data(request):
    four_list = StationFour.objects.order_by('-date_created')
    s4 = Default.objects.get(station="Station 4")
    context = {
        'four_list': four_list,
        's4': s4,
        }
    return render(request, 'four_data.html', context)

def five_data(request):
    five_list = StationFive.objects.order_by('-date_created')
    s5 = Default.objects.get(station="Station 5")
    context = {
        'five_list': five_list,
        's5': s5,
        }
    return render(request, 'five_data.html', context)

def six_data(request):
    six_list = Stationsix.objects.order_by('-date_created')
    s6 = Default.objects.get(station="Station 6")
    context = {
        'six_list': six_list,
        's6': s6,
        }
    return render(request, 'six_data.html', context)

# def updateTolerace(request):
#     if request.POST:
#         station = request.POST.get('station')
#         minimum = request.POST.get('minimum')
#         maximum = request.POST.get('maximum')
#         default = get_object_or_404(Default, station=station)
#         default.minimum = float(minimum)
#         default.maximum = float(maximum)
#         default.save()
#         return redirect('home')