from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Members
from .forms import MembersForm


def members (request):
    error = ''
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Форма заполнена неверно'



    form = MembersForm()
    data = {
        'form':form,
        'error':error

    }

    return render(request, "members/members.html",data)


def members_info (request):
    data = Members.objects.all()
    return render(request, "members/members_info.html",{'data':data})

