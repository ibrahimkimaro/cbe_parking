from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# hapa ndo tunatengeneza views zetu kwny web etu tuna def functionName ndo tunaitumia kwny urls.py kama view. 

def home(Response):
    return HttpResponse("home page")

def about(Response):
    return HttpResponse("achan kxingua bana")


def products(Response):
    return HttpResponse("Try to produce more products")