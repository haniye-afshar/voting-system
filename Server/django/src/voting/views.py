from django.shortcuts import render

sum1 = 0

def home_page(request):
    context ={
        "title" : "voting"
    
    }

    if request.method == 'POST':
        global sum1
        input1 = int(request.POST.get('input1'))
        input2 = int(request.POST.get('input2'))
        
        sum = input1 + input2 + sum1
        sum1 = sum

        print(sum)

           

    return render(request, "home_page.html", context)

