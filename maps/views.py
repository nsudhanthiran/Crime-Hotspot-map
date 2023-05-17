from django.shortcuts import render
from django.http import JsonResponse
from random import random
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random
from . import predction

# Create your views here.
def index(request):
    return  render(request, 'index.html')

@csrf_exempt
def update_marker_coordinates(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')


        # Do something with the latitude and longitude
        coord = (float(latitude), float(longitude))
        progress = predction.predict(coord)

        return JsonResponse({'status': 'success', 'progress': progress})
    else:
        return JsonResponse({'status': 'error'})
    
