import uuid
from core.utils import extract_redirect, generateReferenceNo, initiateRequest, validate_post_data
from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render

 

def index(request):
    return render(request,'pages/index.html')

def donate(request):
    if request.method == "GET" :
        return render(request,'pages/donate.html')

    errors , clean_data = validate_post_data(request)
    if len(errors):
        return render(request,'pages/donate.html', {"errors":errors } )
    

    payload = {
        'amount': clean_data['amount'],
        'reference_number':generateReferenceNo(),
        'transaction_id': uuid.uuid4(),
        'sendSource': True,
        'mobile': clean_data['mobile'],
    }

        

    res =  initiateRequest(payload)
    redirect_url = extract_redirect(res)

    if not redirect_url:
        # Probably some nice UI for a user but this will do for now
        return HttpResponseServerError("Something went wrong, If the problem persists, You are definitely doing something wrong")

        

    if res.status_code == 404 :
        # Something must have gone wrong
        return redirect(redirect_url)

    return redirect(redirect_url)


def handleCallback(request):
     return HttpResponse('Results from beem')
    
    