from django.contrib import admin

# Register your models here.
from . models import ParkingRequest

@admin.register(ParkingRequest)
class parking_record_details(admin.ModelAdmin):
    list_display = ['user','reportTime','departureTime','status_request']
