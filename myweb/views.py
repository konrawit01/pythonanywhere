from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from myweb.models import Question, Travel
from django.utils.regex_helper import Choice
from .models import TravelType

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
	return render(req, 'myweb/user.html')

def united(req):
	return render(req, 'myweb/united.html')

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




def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'myweb/detail.html',{'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



def alltraveltype(request):

    alltraveltype = Travel.objects.all()
    context = {'alltraveltype':alltraveltype }

    return render(request,'myweb/index.html',context)