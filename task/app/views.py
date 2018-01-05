from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    try:
        user = User.objects.get(username=request.session['username'])
    except:
        user = None
    return render(request, 'index.html', {user: user})


def room(request):

    return render(request,'room.html',)