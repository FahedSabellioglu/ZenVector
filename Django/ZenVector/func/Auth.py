from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.http import JsonResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ZenVector.models import *
from EmailHandler import *

"""Login, Signup, PlanBuying"""
def Signup(request):
    """"
        plan buying if the user has no such account previously
        :param
        :returns json response of 200 or 400 status code
    """""
    data = dict(request.POST)
    if not Users.objects.filter(email=data['mail'][0]).exists():
        new_usr = Users.objects.create_user(username=data['name'][0], password=data['pass'][0], email=data['mail'][0])
        new_usr.account_type = data['acc_type'][0]
        new_usr.save()
        message = Email_SignUp(data['mail'][0],data['name'][0],data['acc_type'][0])
        Email_SendServer(message,data['mail'][0])
        login(request, new_usr)
        rtn = JsonResponse({"reason":"Success"})
        rtn.status_code = 200
        return rtn

    rtn = JsonResponse({"message": "Failed", 'reason': "This email address is used"})
    rtn.status_code = 403
    return rtn

def Login(request):
    """
        a logging in function
        :param
        :returns json response with 401 or 200 status code
    """""
    data = dict(request.POST)
    if Users.objects.filter(email=data['mail'][0]).exists():
        obj = Users.objects.get(email=data['mail'][0])
        usr = authenticate(email=obj.email,password=data['password'][0])
        if usr:
            response = JsonResponse({"message":"Success"})
            response.status_code = 200
            login(request,usr)
            return  response
        else:
            response =  JsonResponse({"message": "Failed", 'reason': "Incorrect email or password, Try again."})
            response.status_code = 403
            return response

    response =  JsonResponse({"message":"Failed",'reason':"This email address is not used"})
    response.status_code = 403
    return response

@login_required(login_url='/PutTogether/')
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/PutTogether/')


@login_required(login_url='/PutTogether/')
def DeleteAccount(request):
    data = dict(request.POST)
    print request.user.email
    usr = authenticate(email=request.user.email, password=data['password'][0])
    if usr:
        usr_obj = Users.objects.get(email=usr)
        logout(request)
        usr_obj.delete()
        usr_obj.delete()
        rtn = JsonResponse({"success":"user is deleted"})
        rtn.status_code = 200
        return rtn
    else:
        rtn = JsonResponse({"reason":"Incorrect password"})
        rtn.status_code = 400
        return rtn


