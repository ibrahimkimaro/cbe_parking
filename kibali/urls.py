from django.urls import path
from . import views

# Hapa ndo tunatengeneza urls zetu kufanta navifation 
# path()= is keyword , '' or 'product'= Majina tnayoandika kwenye web tab etu kwnda kwny page yetu , 
# view.home or views.about  views nd tulio import juu hapo kwny tuniat kwa nukt hiii kinachofuat ile namefuction yetu kwny urls.py 

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('product',views.products),
]
 