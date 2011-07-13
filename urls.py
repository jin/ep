from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Django-related/Experimental
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)


# EP-related
urlpatterns += patterns('ep.carparks.views',
        (r'^live/$', 'measurements'),
        (r'^live/(?P<req_cluster>\d{1,2})/$', 'node_request'),
        (r'^live/(?P<req_cluster>\d{1,2})/(?P<req_node>\d{1,2})/$', 'node_request'),
        )
