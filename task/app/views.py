from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    """首頁函數

    Parameters
    ----------
    request

    Returns
    -------

    """
    try:
        user = User.objects.get(username=request.session['username'])
    except:
        user = None

    Rooms=Room.objects.all().order_by('number')[:4]

    return render(request, 'index.html', {user: user,'list': Rooms,'l_post':[1,1]})


def rooms(request):
    """房屋展示函數

    Parameters
    ----------
    request

    Returns
    -------

    """

    return render(request,'rooms.html',{})


def news(request):
    """暫時模塊

    Parameters
    ----------
    request

    Returns
    -------

    """

    return render(request,'news.html',{})