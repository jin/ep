from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def show_clusters(request, template_name='clusters.html'):
    clusters = Cluster.objects.all()
    return render_to_response(template_name, {'clusters': clusters})


@csrf_exempt
def measurements(request, template_name='measurements.html'):
    measurements = Measurement.objects.all()[:10]
    return render_to_response(template_name, {'measurements': measurements})


@csrf_exempt
def add_record(request, req_cluster = 2, req_node = 2, req_reading = 149):
    record = Measurement(node = Node.objects.get(cluster = req_cluster, node = req_node), raw_reading = req_reading)
    record.save()
    return HttpResponse('OK')
