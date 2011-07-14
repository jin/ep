from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from ep.carparks.models import *
from django.views.decorators.csrf import csrf_exempt


def xmlresponse(request, req_cluster):
    return HttpResponse('OK')
