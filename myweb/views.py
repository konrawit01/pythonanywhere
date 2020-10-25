from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Travel, TravelPlaceKeeper , TravelType

# Create your views here.


def contact(req):
	return render(req, 'myweb/contact.html')

def home(req):
	return render(req, 'myweb/home.html')
    
def admins(req):
	return render(req, 'myweb/admins.html')

def index(req):
	return render(req, 'myweb/index.html')

def user(req): 
    showtravel = Travel.objects.all()
    showtravel1 = TravelPlaceKeeper.objects.all()
    
    return render(req, 'myweb/user.html',{'showtravel':showtravel,'showtravel1':showtravel1})

def logins(req):
	return render(req, 'myweb/logins.html')

def traveldo(req):
	return render(req, 'myweb/traveldo.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()

            login(request,user)

            return redirect('logins')
    context['form']=form
    return render(request,'myweb/sign_up.html',context)

