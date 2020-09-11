from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


response={}
names=[]
num = 0
score =0

def home_page(request):
    global scores
    context ={
        "title" : "voting"
    
    }
    return render(request,"home_page.html",context)

def data(request):
    global response,num

    if request.method == "GET":
        name = request.GET.get('value')
        names.append(name)
        name_id = request.session[name] ='%d'%num
        num +=1
        response ={name_id:name}
        
        print(names)

    return JsonResponse(names,safe =False)

def voting_page(request):
    global score
    
    if request.method == "GET":
        for i in range(len(names)-1):
            print(request.GET.get("%s"%names[i]))

    return HttpResponse("")


def polling(request):
    if len(names) == 6:
        return HttpResponse("ali")
