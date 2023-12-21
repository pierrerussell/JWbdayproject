from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import datetime


# Create your views here.
def index(request):
    bday = date(date.today().year, 12, 2)
    if bday == date.today():
        isbday = True
    else:
        isbday = False

    timeleft = datetime.date(date.today().year, 12, 2) - datetime.date.today()

    return render(request, 'jaewonsbday/index.html', {
        'isbday': isbday,
        'timeleft': timeleft
    })
