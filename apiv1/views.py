from django.shortcuts import render_to_response
from ep.carparks.models import *


def xml_response(request):
    if request.method == 'GET':
        req_cluster = int(request.GET["cluster_id"])

        try:
            latest = request.GET["latest"]
            if int(latest) >= 250:
                latest = 250
        except:
            latest = None

        try:
            req_node = int(request.GET["node_id"])
        except:
            req_node = None

        if req_node is None:
            selected_nodes = Node.objects.filter(cluster = req_cluster)
            nodes = []

            for node in selected_nodes:
                nodes.append(node.id)

            if latest:
                measurements = Measurement.objects.filter(node__in=nodes)[:latest]
            else:
                measurements = Measurement.objects.filter(node__in=nodes)

        else:
            selected_node = Node.objects.filter(cluster = req_cluster).get(node = req_node)
            if latest:
                measurements = Measurement.objects.filter(node = selected_node.id)[:latest]
            else:
                measurements = Measurement.objects.filter(node = selected_node.id)

        return render_to_response('measurements.xml', {'measurements': measurements})
