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
up_names={}
controller = []
voters = []

def home_page(request):
    global controller
    global up_names, names
    
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
    
    if request.session["username"] in controller:
        pass
    
    else:
        names[request.session["username"]] = 0
        return HttpResponse('')

def start_voting(request):
    global controller

    controller.append(request.session["username"])

    return HttpResponse('')
    
def reset(request):
    controller.clear()
    names.clear()
    voters.clear()
    return HttpResponse('')
    
def voting_page(request):
    attendees = {}
    attendees = dict(names.items())
    attendees.pop(request.session["username"])

    context={
        'title' : 'voting',
        'attendees' : attendees
    }
    
    return render(request, 'voting_page.html', context)


def result_page(request):
    context ={
        "title" : "Results",
        "controller" : controller,
        "names" : names,
        "session" : request.session["username"],
        "voters" : voters
    }

    return render(request,"results_page.html",context)

@csrf_exempt
def update_score(request):
    global names,voters
    score = 0
    session = request.session["username"]
    up_names = json.loads(request.body.decode('utf-8'))
    
    for x in up_names:
        score += up_names[x]

    if session not in voters and score == 15:
        voters.append(session)
        for x in up_names:
            if x in names:
               names[x] += up_names[x]
        return HttpResponse('ok')
    
    else:
        return HttpResponse('You have already given point' if session in voters 
                             else 'The sum of points must be 15')

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