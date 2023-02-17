from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import User
from django.http import HttpResponseRedirect


from .models import Startups, Contact, Job, Faq

User = get_user_model()

# Create your views here.
def index(request):
    context = {"startups": Startups.objects.filter(admin_approval=True).order_by('-date_approval')[0:4],
    "faqs": Faq.objects.all()}
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def Forgot(request):
    return render(request, 'forgot_password.html')

def Startup(request):
    context = {"startups": Startups.objects.filter(admin_approval=True)}
    return render(request, 'startups.html', context)       


def Career(request):
    context = {"careers": Job.objects.all()}
    return render(request, 'careers.html', context)

def Koech(request):
    # context = {"careers": Job.objects.all()}
    return render(request, 'tables.html')

def Contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message= request.POST['message']
        contact = Contact.objects.create(name = name , email = email, subject = subject, message = message)
        contact.save()
        print('message sent')
        return redirect('/contact')
    return render(request, 'contact.html') 

def Logout(request):
    return redirect('/')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/startup')
        else:
            print( 'Wrong Email or Password')
            return redirect('/login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobile= request.POST['mobile']
        password= request.POST['password']
        user = User.objects.create_user(first_name = first_name, last_name = last_name, 
        password = password , email = email, mobile = mobile)
        user.save()
        print('user created')
        return redirect('/login')
    return render(request, 'register.html')    