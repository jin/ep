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
        (r'^carparks/$', 'show_clusters'),
        (r'^live/$', 'measurements')
        )
