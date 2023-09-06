from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "january",
    "february": "february",
    "march": "march",
    "april": "april",
    "may": "may",
    "june": "june",
    "july": "july",
    "august": "august",
    "september": "september",
    "october": "october",
    "november": "november",
    "december": "december"
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        month_route = months[month - 1]
        return HttpResponseRedirect("/challenges/" + month_route)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge(request, month):
    month_text = None
    try:
        month_text = monthly_challenges[month]
        return HttpResponse(f"{month_text} challenge")
    except:
        return HttpResponseNotFound("This month is not supported!")


