from django.contrib.auth import authenticate , login , get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import LoginForm,RegisterForm
from django.template.response import TemplateResponse

response={}
names=[]
num = 0
score =0
name = ''
name_id =0
session_id = ''
def home_page(request):
    global scores
    context ={
        "title" : "voting"
    
    }
    print(session_id)
    return render(request,"home_page.html",context)

def data(request):
    global response,num,name,name_id

    if request.method == "GET":
        name = request.GET.get('value')
        names.append(name)
        

    return JsonResponse(names,safe =False)

def voting_page(request):
    global score
    
    if request.method == "GET":
        for i in range(len(names)-1):
            print(request.GET.get("%s"%names[i]))

    return HttpResponse("")


def polling(request):
    
        
    
    context ={
        "title" : "voting",
         "names" : names,
         "len" : len(names)
        }
    if len(names) == 3:
        print(name_id)
        return JsonResponse(names,safe =False)



def login_page(request):
    global session_id
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
            session_id = request.session["username"] =username
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
