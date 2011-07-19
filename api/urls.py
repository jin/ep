from django.conf.urls.defaults import *


# Using views.py for API
urlpatterns = patterns('ep.api.views',
        (r'xml/clusters', 'xml_response'),
        )

# Using handlers.py for API for django-piston
#urlpatterns += patterns('ep.api.handlers',
        #(r'xml/clusters', 'xml_response'),
        #)
