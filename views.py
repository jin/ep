from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse 
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def helloworld(request, template_name='helloworld.html'):
    #return render_to_response(template_name)
    if request.method == 'POST':
        return HttpResponse('POST OK')
    elif request.method == 'GET':
        return HttpResponse('GET OK')
    elif request.method == 'PUT':
        return HttpResponse('PUT OK')
    elif request.method == 'DELETE':
        return HttpResponse('DELETE OK')
    else:
        return HttpResponse('No method defined')
