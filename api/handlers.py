from piston.handler import BaseHandler, Emitter
from ep.carparks.models import Node, Measurement


class MeasurementHandler(BaseHandler):
    allowed_methods = ('GET',)

    @classmethod
    def read(self, request):

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

        if req_node: 
            selected_node = Node.objects.filter(cluster = req_cluster).get(node = req_node)
            if latest:
                measurements = Measurement.objects.filter(node = selected_node.id)[:latest]
            else:
                measurements = Measurement.objects.filter(node = selected_node.id)

        else:
            selected_nodes = Node.objects.filter(cluster = req_cluster)
            nodes = []
            for node in selected_nodes:
                nodes.append(node.id)
            if latest:
                measurements = Measurement.objects.filter(node__in=nodes)[:latest]
            else:
                measurements = Measurement.objects.filter(node__in=nodes)

        return measurements


class XMLEmitter(Emitter):
    pass


Emitter.register('xml', XMLEmitter, 'text/xml; charset=utf-8')
