from piston.handler import BaseHandler
from ep.carparks.models import Node, Measurement


class MeasurementHandler(BaseHandler):
    allowed_methods = ('GET','POST')
    model = Measurement

    def read(self, request):
        entries = Measurement.objects

        return entries.all()[:25]
    


