# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connections
from django.shortcuts import render
from database_func import *

cursor = connections['default'].cursor()

def page_Home(response):
    cursor.execute("SELECT * FROM Users")
    data = cursor.fetchall()
    return render(response,'index.html')


def func_login(request):
    data =  dict(request.POST)
    check = add_user(data['name'][0],data['pass'][0],data['mail'][0])
    if check:
        print "YES"
    else:
        print "FALSE"

    return 400


def page_Projects(response):


    return render(response,'project.html')


def page_User(response):


    return render(response,'user.html')









# Create your views here.
