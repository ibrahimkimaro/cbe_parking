from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class parking_record_details(admin.ModelAdmin):
    list_display = ['user','plate_number']
