from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *


def xml_response(request):
    if request.method == 'GET':
        req_cluster = request.GET["cluster_id"]

        try:
            latest = request.GET["latest"]
            if int(latest) >= 250:
                latest = 250
        except:
            latest = None

        selected_nodes = Node.objects.filter(cluster = req_cluster)
        nodes = []

        for node in selected_nodes:
            nodes.append(node.id)

        if latest is not None:
            measurements = Measurement.objects.filter(node__in=nodes)[:latest]
        else:
            measurements = Measurement.objects.filter(node__in=nodes)[:250]

        return render_to_response('measurements.xml', {'measurements': measurements})
