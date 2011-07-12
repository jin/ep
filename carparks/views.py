from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *
from django.views.decorators.csrf import csrf_exempt
from xml.etree import ElementTree


@csrf_exempt
def measurements(request, template_name='measurements.html'):
    measurements = Measurement.objects.all()[:10]
    return render_to_response(template_name, {'measurements': measurements})


@csrf_exempt
def record(request, req_cluster, req_node, req_reading):
    try:
        req_cluster, req_node, req_reading = int(req_cluster), int(req_node), int(req_reading)
    except ValueError:
        raise Http404()
    record = Measurement(node = Node.objects.get(cluster = req_cluster, node = req_node), raw_reading = req_reading)
    record.save()
    return HttpResponse('OK')


@csrf_exempt
def node_request(request, req_cluster, req_node):
    try:
        req_cluster, req_node, = int(req_cluster), int(req_node)
    except ValueError:
        raise Http404()

    if request.method == 'POST':
        tree = ElementTree.fromstring(request.raw_post_data)
        for element in tree.getiterator():
            if element.tag == 'reading':
                req_reading = int(element.text)
        record = Measurement(node = Node.objects.get(cluster = req_cluster, node = req_node), raw_reading = req_reading)
        record.save()
        return HttpResponse('OK\n')

    elif request.method == 'GET':
        measurements = Measurement.objects.filter(node = req_node)
        return render_to_response('measurements.html', {'measurements': measurements})

    else:
        raise Http404()
