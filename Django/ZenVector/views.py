# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.shortcuts import render
from models import *
from django.http import JsonResponse
def page_Home(response):
    #
    # per = Projects(project_name="NEW PROJECT 2",usr_email=Users.objects.get(email='fahedshabani@std.sehir.edu.tr'))
    # per.save()
    return render(response,'index.html')


def func_login(resquest):
    data = dict(resquest.POST)
    if Users.objects.filter(email=data['mail'][0]).exists():
        obj = Users.objects.get(email=data['mail'][0])
        if data['password'][0] == obj.password and data['mail'][0] == obj.email:
            response = JsonResponse({"message":"Success"})
            response.status_code = 200
            return  response
        else:
            response =  JsonResponse({"message": "Failed", 'reason': "Incorrect email or password, Try again."})
            response.status_code = 401
            return response

    response =  JsonResponse({"message":"Failed",'reason':"This email address is not used"})
    response.status_code = 401
    return response


def func_signup(request):
    data =  dict(request.POST)
    if Users.objects.filter(email=data['mail']).exists():
        print "exits"
        return JsonResponse({"message":"Failed",'reason':"This email address is used"})

    else:
        new_usr = Users.objects.create(usr_name=data['name'][0],password=data['pass'][0],email=data['mail'][0])
        new_usr.save()
        print "data"
        return JsonResponse({"message":"Success"})


def page_Projects(response):


    return render(response,'project.html')


def page_User(response):


    return render(response,'user.html')









# Create your views here.
