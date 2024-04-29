from django.contrib import admin
from . models import User

@admin.register(User)
class UserRegistration(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email','phone_number','status','status_type','password','date_joined','is_active','is_staff']


# Register your models here.
