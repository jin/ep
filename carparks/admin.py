from django.contrib import admin
from ep.carparks.models import Cluster, Node, Measurement



class ClusterAdmin(admin.ModelAdmin):
    list_display = ('name',)



class NodeAdmin(admin.ModelAdmin):
    list_display = ('cluster', 'node')
    ordering = ('cluster', 'node',)



class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('node', 'raw_reading', 'batt', 'created')
    ordering = ('-created',)


admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(Measurement, MeasurementAdmin)
