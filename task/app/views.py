from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .unit import islogin


# Create your views here.


def index(request):
    """首頁函數
    """
    user = islogin(request)

    rooms = Room.objects.all().order_by('number')[:4]
    posts = Latest_post.objects.all().order_by('time')[:2]

    return render(request, 'index.html', {'user': user, 'list': rooms, 'l_post': posts, 'index': True})


def rooms(request):
    """房屋展示函數
    """
    user = islogin(request)
    rooms = True
    return render(request, 'rooms.html', {'user': user, 'rooms': rooms})


def news(request):
    """新聞模塊
    """
    user = islogin(request)
    return render(request, 'news.html', {'user': user, 'news': True})


def article(request):
    """文章模塊
    """
    user = islogin(request)
    actical = Latest_post.objects.filter(id=request.GET['id'])
    return render(request, 'article.html', {'user': user, 'acticals': actical})


def gallery(request):
    """酒店環境頁面
    """
    user = islogin(request)
    posts = Latest_post.objects.all().order_by('time')[:2]
    return render(request, 'gallery.html',
                  {'user': user, 'fadeleft': [1, 2, 3, 4], 'faderight': [1, 2, 3, 4], 'l_post': posts, 'gallery': True})


def email(request):
    """提交郵箱
    """
    # TODO 獲取郵箱並返回當前頁
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def user(request):
    """用户操作函数
    """
    # TODO do=login 登陆 do=register

    if request.GET['do']=='register':
        return render(request,'register.html',{})
    elif request.GET['do']=='login':


        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
