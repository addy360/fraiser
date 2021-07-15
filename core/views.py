from django.shortcuts import render


def index(request):
    return render(request,'pages/index.html')

def donate(request):
    return render(request,'pages/donate.html')
    
    
    