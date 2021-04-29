from django.shortcuts import render
from django.http import HttpResponse
from .models import Coffee

def coffee (request):

    return render(request, "coffee/coffee.html")


def coffee_info(request):
    data = Coffee.objects.all()
    #coffee_list = [i for i in data.values()]
    #return HttpResponse(f"Chai table:{coffee_list}")
    return render(request,"coffee/coffee_info.html",{'data':data})
