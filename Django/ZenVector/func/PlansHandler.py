from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ZenVector.models import *


@login_required(login_url='/PutTogether/')
def upgrade_account(request):
    """
     HAS SOME BUGS, WAITING FOR PROJECTS PAGE
    :param request:
    :return:
    """""
    data = dict(request.POST)
    usrObj = Users.objects.get(email=request.user)
    if usrObj.account_type == 'F':
        usrObj.account_type = "P"
    elif usrObj.account_type == 'P':
        usrObj.account_type = "B"
    usrObj.save()

    rtn = JsonResponse({"message":"has been upgraded"})
    rtn.status_code = 200
    #TODO
    #send email

    return rtn

@login_required(login_url="/PutTogether/")
def plan_downgrade(request):
    """"
        downgrading the user plan, the user has to be logged in
        :returns josn response fo 401 or 200
    """""
    data = dict(request.POST)
    usrObj = Users.objects.get(email=request.user)
    to_account_type = data['account_type'][0]
    projects_count = len(Projects.objects.filter(usr_email=usrObj))
    if (to_account_type == "F" and projects_count > 5) or (to_account_type == "P" and projects_count > 500)  :
        rtn = JsonResponse({"reason":"Reduce the number of projects you have"})
        rtn.status_code = 401
        return rtn
    usrObj.account_type = data['account_type'][0]
    usrObj.save()
    rtn = JsonResponse({"message":"has been downgraded"})
    rtn.status_code = 200
    return rtn
