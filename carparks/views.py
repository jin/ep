from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *
from django.views.decorators.csrf import csrf_exempt
from xml.etree import ElementTree


def measurements(request, template_name='measurements.html'):
    measurements = Measurement.objects.all()[:10]
    return render_to_response(template_name, {'measurements': measurements})


@csrf_exempt
def node_request(request, req_cluster, req_node=None):
    if req_node == None:
        try:
            req_cluster = int(req_cluster)
        except ValueError:
            raise Http404()
    else:
        try:
            req_cluster, req_node, = int(req_cluster), int(req_node)
        except ValueError:
            raise Http404()

    if request.method == 'POST':
        tree = ElementTree.fromstring(request.raw_post_data)
        for element in tree.getiterator():
            if element.tag == 'reading':
                req_reading = int(element.text)
        entry = Measurement(node = Node.objects.get(cluster = req_cluster, node = req_node), raw_reading = req_reading)
        entry.save()
        return HttpResponse('OK\n')

    elif request.method == 'GET':
        if req_node != None:
            selected_node = Node.objects.filter(cluster = req_cluster).get(node = req_node)
            measurements = Measurement.objects.filter(node = selected_node.id)
        else:
            selected_nodes = Node.objects.filter(cluster = req_cluster)
            print type(selected_nodes)
            nodes = []
            for node in selected_nodes:
                nodes.append(node.id)
            measurements = Measurement.objects.filter(node__in=nodes)

        return render_to_response('measurements.html', {'measurements': measurements})

    else:
        raise Http404()
