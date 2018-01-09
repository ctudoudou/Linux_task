#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/9 上午8:54
# @Author  : tudoudou
# @File    : unit.py
# @Software: PyCharm

from .models import *


def islogin(request):
    try:
        user = User.objects.get(username=request.session['username'])
    except:
        user = None

    return user