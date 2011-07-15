from django.conf.urls.defaults import *


urlpatterns = patterns('ep.api.handlers',
        (r'/xml/clusters', 'xml_response'),
        )
