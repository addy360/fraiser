from core.utils import validate_post_data
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'pages/index.html')

def donate(request):
    if request.method == "GET" :
        return render(request,'pages/donate.html')

    errors , clean_data = validate_post_data(request)
    if len(errors):
        return HttpResponse('Validation errors')
        
    print(clean_data)
    return HttpResponse('Thank you for your donations')
    
    
    