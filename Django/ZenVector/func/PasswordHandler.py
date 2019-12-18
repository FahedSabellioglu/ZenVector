from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from ZenVector.models import *
from EmailHandler import  *


def NonLogged_ResetPassword(request):
    """"
        changes the password of the user after passing all the checks.
        :param
        :returns json response of 200 status code
    """""
    data = dict(request.POST)
    user_obj = Users.objects.get(email=data['email'][0])
    user_obj.set_password(data['password'][0])
    user_obj.save()
    codeObjct  = PasswordCodes.objects.get(usr_email=user_obj,code=data['code'][0])
    codeObjct.isUsed = True
    codeObjct.save()
    rtn = JsonResponse({"message":'password changed'})
    rtn.status_code = 200
    return  rtn

@login_required(login_url='/PutTogether/')
def Logged_change_password(response):
    """
        changing the password for a logged in user
        :returns
        json response of 200(succeed) status code
    """
    data = dict(response.POST)
    user_obj =Users.objects.get(email=response.user.email)
    user_obj.set_password(data['password'][0])
    update_session_auth_hash(response, response.user)
    user_obj.save()
    print response.user
    rtn = JsonResponse({"message":'password changed'})
    rtn.status_code = 200
    return  rtn


def PasswordResetLink(response,email,code):
    """
    check 
    :param response:
    :return:
    """""

    code_object = PasswordCodes.objects.filter(usr_email=email,code=code)
    if len(code_object) != 0:
        return render(response,'index.html',{'Available':True,'check':code_object[0].isUsed})

    return render(response,'index.html',{"Available":False})

def RequestPasswordResetCode(request):
    """
        gets the user entered email and checks if there such user, sends a code for resetting password to his email
        :returns json response of 200 or 401 status code
    """""
    data = dict(request.POST)
    usr = Users.objects.filter(email=data['usr_email'][0])
    if len(usr) != 0:
        PasswordCodes.objects.filter(usr_email=usr[0]).delete()
        password_code = PasswordCodes(usr_email=usr[0])
        password_code.save()
        message = Email_PasswordResetCode(usr[0].email,password_code.code)
        Email_SendServer(message,usr[0].email)
        rtn = JsonResponse({"message": "email has been sent"})
        rtn.status_code = 200
        return rtn
    rtn = JsonResponse({"reason":"Email does't belong to an account"})
    rtn.status_code = 401
    return rtn

def PasswordResetCodeValidity(request):
    """
        a function for checking if the code given by the user if the code we have sent him/her
        :param request:
        :return: json response of 200 or 404
    """""
    data = dict(request.POST)
    usr = Users.objects.get(email=data['usr_email'][0])
    code = PasswordCodes.objects.get(usr_email=usr)
    if  code.code == data['code'][0]:
        code.delete()
        rtn = JsonResponse({"message": "Correct Code"})
        rtn.status_code = 200
        return rtn

    rtn = JsonResponse({"reason": "Wrong Code, Try again"})
    rtn.status_code = 404
    return rtn