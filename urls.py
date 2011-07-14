from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Django-related/Experimental
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)


# EP main web view
urlpatterns += patterns('ep.carparks.views',
        (r'^live/$', 'measurements'),
        (r'^live/(?P<req_cluster>\d{1,2})/$', 'node_request'),
        (r'^live/(?P<req_cluster>\d{1,2})/(?P<req_node>\d{1,2})/$', 'node_request'),
        (r'^m/$', 'mobile_ui_main'),
        (r'^m/(?P<req_cluster>\d{1,2})/$', 'mobile_ui_cluster_overview'),
        (r'^xml/(?P<req_cluster>\d{1,2})/$', 'render_xml'),
        )


# EP API version 1.0
urlpatterns += patterns('ep.apiv1.views',
        (r'^api/v1/xml/(?P<req_cluster>\d{1,2})/$', 'xmlresponse'),
        )
