from django.shortcuts import render
from django.http import HttpResponse
from .models import Chai

def tea (request):

    return render(request, "tea/tea.html")


def tea_info(request):
    data = Chai.objects.all()
    #chai_list = [i for i in data.values()]
    #return HttpResponse(f"Chai table:{chai_list}")
    return render(request,"tea/tea_info.html",{'data':data})
