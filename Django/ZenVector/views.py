# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections
from django.http import HttpResponse

from django.shortcuts import render

def page_Home(response):
    cursor = connections['default'].cursor()
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    return render(response,'index.html')


def func_login(response):
    print response.GET,'function'
    return None


def page_Projects(response):


    return render(response,'project.html')


def page_User(response):


    return render(response,'user.html')









# Create your views here.
