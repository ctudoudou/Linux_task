from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    """首頁函數
    """
    try:
        user = User.objects.get(username=request.session['username'])
    except:
        user = None

    rooms = Room.objects.all().order_by('number')[:4]
    posts = Latest_post.objects.all().order_by('time')[:2]

    return render(request, 'index.html', {user: user, 'list': rooms, 'l_post': posts, 'index': True})


def rooms(request):
    """房屋展示函數
    """

    rooms = True
    return render(request, 'rooms.html', {'rooms': rooms})


def news(request):
    """暫時模塊
    """

    return render(request, 'news.html', {})


def article(request):
    """文章模塊
    """

    actical = Latest_post.objects.filter(id=request.GET['id'])
    return render(request, 'article.html', {'acticals': actical})
