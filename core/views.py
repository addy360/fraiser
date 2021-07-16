from core.models import Donation, Profile
import uuid
from core.utils import extract_redirect, generateReferenceNo, initiateRequest, validate_post_data
from django.http.response import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render

 

def index(request, username):
    profile = Profile.objects.select_related('user').first()
    context = { 'profile': profile }
    return render(request,'pages/index.html', context)

def donate(request, profile_id):
    context = { "profile_id" : profile_id  }
    if request.method == "GET" :
        return render(request,'pages/donate.html', context)

    errors , clean_data = validate_post_data(request)
    if len(errors):
        return render(request,'pages/donate.html', {"errors":errors, **context } )
    
    donation = Donation()
    donation.transaction_id = uuid.uuid4()
    donation.reference_number = generateReferenceNo()
    donation.amount = clean_data['amount']
    donation.mobile =  clean_data['mobile']
    donation.profile = Profile.objects.first()
    donation.donator = clean_data['donator']

    donation.save()

    payload = {
        'amount': donation.amount,
        'reference_number':donation.reference_number,
        'transaction_id': donation.transaction_id,
        'sendSource': True,
        'mobile': donation.mobile,
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
    
    