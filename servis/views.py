from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from .models import Product
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse('Hello Syn')

def page(request, pageNum):
    return HttpResponse(f'Page {pageNum}')

def about(request, id):
    try:
        var = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Http404('Not Found')

    return HttpResponse("Okay")
