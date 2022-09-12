from email import message
import email
from unicodedata import name
from django import views
from django.shortcuts import render
from .models import *



# Create your views here.

def base():
    view={}
    view['feedbacks']=Feedback.objects.all()
    view['informations']=Informations.objects.all()
    view['message']='Your message is sent'
    return view


def index(request):
    view={}
    # view['feedbacks']=Feedback.objects.all()
    return render(request, 'index.html',base())

def about(request):
    return render(request, 'about.html')

def contact(request):
    view={}
    # view['informations']=Informations.objects.all()
    if request.method=="POST":
        view={}
        na=request.POST['name']
        em=request.POST['email']
        sub=request.POST['subject']
        mes=request.POST['message']
        data=Contact.objects.create(
            name= na,
            email= em,
            subject=sub,
            message= mes


        )
        data.save()
        view=base()
        view.update({'message':'success '})
        # view['message']='Your message is sent'
        
        return render(request, 'contact.html',view)
        

    return render(request, 'contact.html', base())

def price(request):
    return render(request, 'price.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def services(request):
    return render(request, 'services.html')


