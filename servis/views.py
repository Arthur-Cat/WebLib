from django.http import HttpResponse, Http404, FileResponse, JsonResponse
from django.urls import reverse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.shortcuts import render

def index(request): 
    #template = get_template('index.html')
    return render(request, 'index.html')

def page(request, pageNum):
    return HttpResponse(f'Page {pageNum}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Http404('Not Found')

    return HttpResponse("Okay")

def jsonShow(request):
    data = {'cost':14, 'title':'Book'}
    return JsonResponse(data)

