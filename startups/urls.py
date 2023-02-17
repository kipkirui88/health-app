from django.urls import path

from . import views
from . import dashboardViews

urlpatterns = [
    path('', views.index, name='index'),
    path('forgot_password/', views.Forgot, name='forgot'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('register/', views.register, name='register'),
    path('startups/', views.Startup, name='startups'),
    path('contact/', views.Contacts, name='contact'),
    path('about/', views.about, name='about'),
    path('career/', views.Career, name='career'),
    path('koech/', views.Koech, name='koech'),


    path('startup/', dashboardViews.startup, name='startup'),
    path('profile/', dashboardViews.profile, name='profile'),
    path('startup/', dashboardViews.index, name='index'),
    path('PostJob/', dashboardViews.jobs, name='jobs'),
    path('profile_update/', dashboardViews.profile_update, name='profile_update'),
    ]