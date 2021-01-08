from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from api.models import ShutdownValve

def home(request):

    valve_list = ShutdownValve.objects.order_by('-created_on')
    context = {'valve_list': valve_list}
    return render(request, 'home.html', context)