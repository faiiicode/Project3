from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Portfolio


def demo(request):
    obj = Place.objects.all()
    obj2= Portfolio.objects.all()
    return render(request, "index.html", {'result': obj,'panel':obj2})



