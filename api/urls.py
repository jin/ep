from django.conf.urls.defaults import *
from piston.resource import Resource
from ep.api.handlers import MeasurementHandler


# Using views.py for API
urlpatterns = patterns('ep.api.views',
        (r'xml/clusters', 'process_xml'),
        )

measurement_handler = Resource(MeasurementHandler)
# Using handlers.py for API for django-piston
urlpatterns += patterns('',
        (r'piston/clusters', measurement_handler),
        )
