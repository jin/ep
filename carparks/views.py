from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse 
from ep.carparks.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def show_clusters(request, template_name='clusters.html'):
    clusters = Cluster.objects.all()
    return render_to_response(template_name, {'clusters': clusters})


@csrf_exempt
def measurements(request, template_name='measurements.html'):
    measurements = Measurement.objects.all()
    return render_to_response(template_name, {'measurements': measurements})


@csrf_exempt
def new_measurement(request, node, raw_reading):
    pass
