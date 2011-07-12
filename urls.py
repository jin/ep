from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)


'''Experimental'''
urlpatterns += patterns('ep.views',
        (r'^helloworld/$', 'helloworld'),
        )


''' Easypark '''
urlpatterns += patterns('ep.carparks.views',
        (r'^live/$', 'measurements'),
        (r'^(?P<req_cluster>\d{1,2})/(?P<req_node>\d{1,2})/(?P<req_reading>\d{1,3})/$', 'record'),
        (r'^(?P<req_cluster>\d{1,2})/(?P<req_node>\d{1,2})/$', 'node_request'),
        )
