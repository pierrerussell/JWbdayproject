from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here.
def index(request):
    bday = date(date.today().year, 12, 2)
    if bday == date.today():
        isbday = True
    else:
        isbday = False

    return render(request, 'jaewonsbday/index.html', {
        'isbday': isbday
    })