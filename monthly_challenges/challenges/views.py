from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

from django.urls import reverse



def index(request):

    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


monthly_challenges={

    "january":"eat no meat",
    "february":"learn django atleast 2min every day",
    "march":"learn django atleast 3min every day",
    "april":"learn django atleast 4min every day",
    "may":"learn django atleast 5min every day",
    "june":"learn django atleast 6min every day",
    "july":"learn django atleast 7min every day",
    "august":"learn django atleast 8min every day",
    "september":"learn django atleast 9min every day",
    "october":"learn django atleast 10min every day",
    "november":"learn django atleast 11min every day",
    "december":"learn django atleast 12min every day"
    
    }



# Create your views here.


def monthly_challenge_by_number(request, month):
     months = list(monthly_challenges.keys())

     if month > len(months):
        return HttpResponseNotFound("invalid Month")

     redirect_month = months[month-1]
     redirect_path = reverse("month-challenge", args=[redirect_month])
     return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
       challenge_text = monthly_challenges[month]
       response_data = f"<h1>{challenge_text}</h1>"
       return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")

    

    # if month == "january":
    #     challenge_text = "walk at 20 minutes every month"
    
    # elif month == "february":
    #     challenge_text = "learn django atleast 30min every day"
    
    # elif month =="march":
    #     challenge_text = "learn django atleast 40min every day"
    
    # else:
    #     return HttpResponseNotFound("THIS MONTH IS NOT SUPPORTED")

    # return HttpResponse(challenge_text)