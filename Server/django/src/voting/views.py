from django.shortcuts import render
from django.http import HttpResponse


sum1 = 0
names = []

def voting_page(request):
        
    
    context ={
        "title" : "voting"
    
    }
    
    input1 = 0
    if request.method == 'POST':
        global sum1
        
        for i in len(names) - 1:
            input1 += int(request.POST.get("input"))
        
            sum = input1 + sum1
            sum1 = sum

            print(sum)

        return render(request,"voting_page.html")
        
def data(request):
    return HttpResponse('%d'%len(names))


def home_page(request):
    global names
    context ={
        "title" : "voting"
    
    }
    
    if request.method == 'POST':
        name = request.POST.get('input')
        names.append(name)
        print(names)


    return render(request,"home_page.html",context)

def vote(request):
    return HttpResponse("the total score is %d"%sum1)