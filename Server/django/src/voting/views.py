from django.contrib.auth import authenticate , login , get_user_model , logout
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import LoginForm,RegisterForm
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
import json

names={}


def home_page(request):
    
    context ={
        "title" : "voting",
    }
    if request.user.is_authenticated == True:
        context["session_id"] = request.session["username"] 
        
        
    else:
        return redirect('login/')

    return render(request,"home_page.html",context)

def add_element(request):
    global names
    
    if request.session["username"] in names:
        pass
    
    else:
        names[request.session["username"]] = 0
        print(names)
        return HttpResponse('')

def start_voting(request):
    return HttpResponse('')
    
def voting_page(request):
    attendees = {}
    attendees = dict(names.items())
    attendees.pop(request.session["username"])
    print(names)
    print(attendees)

    context={
        'title' : 'voting',
        'attendees' : attendees
    }
    
    return render(request, 'voting_page.html', context)

def submit(request):
    attendees = {}
    attendees = dict(names.items())
    attendees.pop(request.session["username"])
    
    
    return JsonResponse(attendees)

@csrf_exempt
def update_score(request):
    if request.is_ajax():
        if request.method == 'POST':
            print ('Raw Data:', request.body.decode('utf-8')) #this type is str
            #print ('Raw Data:', json.loads(request.body.decode('utf-8'))) #this type is json
            print ('type(request.body):', type(request.body)) # this type is bytes

    return HttpResponse('')

def login_page(request):
    print(f" is user loged in : {request.user.is_authenticated}")
    form = LoginForm(request.POST or None)
    context ={
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username = username , password = password)
        if user is not None:
            login(request,user)
            context['form'] = form
            request.session["username"] =username
            return redirect('/')
        else:
            print("error")

    return render(request,"auth/login.html",context)

User = get_user_model()

def register_page(request):
    form = RegisterForm(request.POST or None)
    context ={
        "form" : form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username = username,email = email,password = password)
        new_user.save()
        print(new_user)
    return render(request,"auth/register.html",context)


def logout_view(request):
    logout(request)
    return redirect('/')