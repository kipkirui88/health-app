from django.contrib import admin

# Register your models here.
from .models import Startups, Contact, Job, Faq

class StartupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'contact', 'location', 'description', 'admin_approval', 'date_approval')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'contact', 'location', 'description', 'company_logo', 'date')

class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')

admin.site.register(Startups, StartupsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Faq, FaqAdmin)
# admin.site.register(User)