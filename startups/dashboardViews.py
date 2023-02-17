from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from django.http import HttpResponseRedirect

from .models import Startups, Job
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
                 
def jobs(request):
    if request.method == "POST":
        form = JobForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
        return render(request, 'index.html',{'obj':obj})
    else:
        form=JobForm()
        img=Job.objects.all()
        return render(request, 'post_job.html',{'img':img, 'form':form})
   

def profile_update(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user = User.objects.get(id=request.user.id)
        user.email = email
        user.firstname = first_name
        user.lastname = last_name
        user.save()
        print('user updated')
        return redirect('/profile') 

def Logout(request):
    return redirect('/')
 