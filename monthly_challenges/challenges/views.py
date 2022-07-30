from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "walk at 20 minutes every month"
    
    elif month == "february":
        challenge_text = "learn django atleast 30min every day"
    
    elif month =="march":
        challenge_text = "learn django atleast 40min every day"
    
    else:
        return HttpResponseNotFound("THIS MONTH IS NOT SUPPORTED")

    return HttpResponse(challenge_text)