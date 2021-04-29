from django.http import HttpResponse
from django.shortcuts import render

def main (request):

    return render(request, "main_1.html")


def autor_info (request):

    return render(request, "autor_info.html")