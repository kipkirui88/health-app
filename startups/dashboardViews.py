from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from django.http import HttpResponseRedirect
from .forms import StartupsForm, JobForm

# Create your views here.


def startup(request):
    context = {'startups': Startups.objects.all()}
    return render(request, 'dashboard.html', context)


def index(request):
    if request.method == "POST":
        form = StartupsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return render(request, 'index.html',{'obj':obj})
    else:
        form=StartupsForm()
        img=Startups.objects.all()
        return render(request, 'post_startup.html',{'img':img, 'form':form})
              

def Logout(request):
    return redirect('/')
 
