from django.shortcuts import render_to_response
from ep.carparks.models import *
from xml.etree import ElementTree
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404, HttpResponse, HttpResponseRedirect



@csrf_exempt
def process_xml(request):
    if request.method == 'GET':
        try:
            req_cluster = int(request.GET["cluster_id"])
        except:
            req_cluster = None
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

        if req_node and req_cluster: 
            selected_node = Node.objects.filter(cluster = req_cluster).get(node = req_node)
            if latest:
                measurements = Measurement.objects.filter(node = selected_node.id)[:latest]
            else:
                measurements = Measurement.objects.filter(node = selected_node.id)

        elif req_node and latest and not req_cluster:
            return HttpResponse("Please specify the cluster_id.")

        elif req_cluster:
            selected_nodes = Node.objects.filter(cluster = req_cluster)
            nodes = []
            for node in selected_nodes:
                nodes.append(node.id)
            if latest:
                measurements = Measurement.objects.filter(node__in=nodes)[:latest]
            else:
                measurements = Measurement.objects.filter(node__in=nodes)

        elif latest:
            measurements = Measurement.objects.all()[:latest]

        else:
            measurements = Measurement.objects.all()[:50]

        return render_to_response('measurements.xml', {'measurements': measurements})

    elif request.method == 'POST':
        tree = ElementTree.fromstring(request.raw_post_data)
        for element in tree.getiterator():
            if element.tag == 'reading':
                req_reading = int(element.text)
            if element.tag == 'batt':
                req_batt = int(element.text)
            if element.tag == 'seq':
                req_seq = int(element.text)
            if element.tag == 'node':
                req_node = int(element.text)
            if element.tag == 'cluster':
                req_cluster = int(element.text)

        entry = Measurement(node = Node.objects.get(cluster = req_cluster, node = req_node), raw_reading = req_reading, batt = req_batt, seq = req_seq)
        entry.save()

        return HttpResponse('OKAY\n')
