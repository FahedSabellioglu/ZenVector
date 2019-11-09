# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.contrib.auth import login,logout,authenticate
from models import *
from django.http import JsonResponse,HttpResponseRedirect
def page_Home(response):
    # logout(response)
    return render(response,'index.html')

def func_logout(request):

    logout(request)
    return HttpResponseRedirect('/PutTogether/')

def func_create_project(request):
    data = dict(request.POST)
    usrObj= Users.objects.get(email='fahedshabani@std.sehir.edu.tr')
    project = Projects(usr_email=usrObj,project_name=data['p_name'][0])
    project.save()
    rtn  = JsonResponse({'message':"created"})
    rtn.status_code = 200
    return  rtn


def func_login(request):
    data = dict(request.POST)
    print data,'new'
    if Users.objects.filter(email=data['mail'][0]).exists():
        obj = Users.objects.get(email=data['mail'][0])
        auth_obj = EmailAuthenticate()
        usr = authenticate(email=obj.email,password=data['password'][0])
        if usr is not None:
            response = JsonResponse({"message":"Success"})
            response.status_code = 200
            login(request,usr)
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
    if Users.objects.filter(email=data['mail'][0]).exists():
        rtn = JsonResponse({"message":"Failed",'reason':"This email address is used"})
        rtn.status_code = 201
        return rtn

    else:
        new_usr = Users.objects.create_user(username=data['name'][0],password=data['pass'][0],email=data['mail'][0])
        rtn = JsonResponse({"message":"Success"})
        rtn.status_code = 200
        return rtn


def page_Projects(response):


    return render(response,'project.html')


def page_User(response):

    return render(response,'user.html')









# Create your views here.
