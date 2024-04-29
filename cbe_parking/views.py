# views.py

from django.http import HttpResponse
from django.conf import settings
import os

def default_image_api(request):
    default_image_path ='images\\profile_pic\\default.png'
    with open(default_image_path, 'rb') as image_file:
        return HttpResponse(image_file.read(), content_type="image/png")
