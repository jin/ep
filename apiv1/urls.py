from django.conf.urls.defaults import *


urlpatterns = patterns('ep.apiv1.handlers',
        (r'/v1/xml/clusters', 'xml_response'),
        )
