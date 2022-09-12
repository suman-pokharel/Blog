from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('price/',views.price,name='price'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('services/',views.services,name='services'),

]


