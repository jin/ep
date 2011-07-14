from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *


def xml_response(request, req_cluster):
    if request.method == 'GET':
        selected_nodes = Node.objects.filter(cluster = req_cluster)
        nodes = []
        for node in selected_nodes:
            nodes.append(node.id)
        measurements = Measurement.objects.filter(node__in=nodes)[:10]

    return render_to_response('measurements.xml', {'measurements': measurements})
