# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.contrib.auth import login,logout,authenticate
from models import *
from django.http import JsonResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth import update_session_auth_hash
import json
"""Password Resetting"""
def forgot_pass(request):
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

def CodeChecker(request):
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

def ResetPassword(request):
    """"
        changes the password of the user after passing all the checks.
        :param
        :returns json response of 200 status code
    """""

    data = dict(request.POST)
    user_obj =Users.objects.get(email=data['email'][0])
    user_obj.set_password(data['password'][0])
    user_obj.save()
    rtn = JsonResponse({"message":'password changed'})
    rtn.status_code = 200
    return  rtn


def page_Home(response):
    for usr in Users.objects.all():
        # if usr.email == 'fahed.sh98@gmail.com':
        #     usr.delete()
        print usr.email
    return render(response,'index.html')



"""Login, Signup, PlanBuying"""
def func_signup(request):
    """"
        signing up a new user, Free version only
    :param request
    :returns json response 400 or 200 status code
    """""
    data =  dict(request.POST)
    if Users.objects.filter(email=data['mail'][0]).exists():
        rtn = JsonResponse({"message":"Failed",'reason':"This email address is used"})
        rtn.status_code = 400
        return rtn

    else:
        new_usr = Users.objects.create_user(username=data['name'][0],password=data['pass'][0],email=data['mail'][0])
        new_usr.account_type = data['acc_type'][0]
        message  = Email_SignUp(data['mail'][0],data['name'][0],data['acc_type'][0])
        Email_SendServer(message,data['mail'][0])
        # new_usr.save()
        # login(request,new_usr)
        # rtn = JsonResponse({"message":"Success"})
        # rtn.status_code = 200
        # return rtn

def func_login(request):
    """
        a logging in function
        :param
        :returns json response with 401 or 200 status code
    """""
    data = dict(request.POST)
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

def plan_register(request):
    """"
        plan buying if the user has no such account previously
        :param
        :returns json response of 200 or 400 status code
    """""
    data = dict(request.POST)
    if not Users.objects.filter(email=data['mail'][0]).exists():
        new_usr = Users.objects.create_user(username=data['name'][0], password=data['password'][0], email=data['mail'][0])
        new_usr.account_type = data['acc_type'][0]
        new_usr.save()
        message = Email_SignUp(data['mail'][0],data['name'][0],data['acc_type'][0])
        Email_SendServer(message,data['mail'][0])
        login(request, new_usr)
        rtn = JsonResponse({"reason":"Success"})
        rtn.status_code = 200
        return rtn

    rtn = JsonResponse({"message": "Failed", 'reason': "This email address is used"})
    rtn.status_code = 400
    return rtn


@login_required(login_url='/PutTogether/')
def func_logout(request):
    logout(request)
    return HttpResponseRedirect('/PutTogether/')

""""""



"""Tasks Functions"""
@login_required(login_url='/PutTogether/')
def fun_new_task(response,p_id):
    """:param
        p_id: project id
        :returns
        json response of 200(succeed) or 404(fail) status code
    """
    data = dict(response.POST)
    proj_obj = Projects.objects.get(project_id=p_id)
    state_obj = state.objects.get(state_id=data['list_name'][0],project_id=proj_obj)

    if Tasks.objects.filter(task_name=data['title'][0],task_project_id=proj_obj).exists():
        response = JsonResponse({"message":"The task already exists"})
        response.status_code = 404
        return  response
    new_task = Tasks(task_name=data['title'][0],task_project_id=proj_obj,task_descrip = data['descrip'][0],
                     task_given_by = proj_obj.usr_email,task_state=state_obj,task_deadline=data['date'][0])
    new_task.save()

    response = JsonResponse({})
    response.status_code = 200
    return response

@login_required(login_url='/PutTogether/')
def func_delete_task(response,p_id):
    """:param
        p_id: project id
        :returns
        json response of 200(succeed) status code
    """
    data = dict(response.POST)
    proj_obj = Projects.objects.get(project_id=p_id)
    task_obj = Tasks.objects.get(task_id=data['taskid'][0],task_project_id=proj_obj)
    task_obj.delete()

    response = JsonResponse({"message":"task has been deleted"})
    response.status_code = 200
    return response

@login_required(login_url='/PutTogether/')
def change_task_details(request,p_id):
    """
        changing the task details
        :param
        p_id: project id
        :returns
        json response of 200(succeed) status code
    """
    data = dict(request.POST)

    proj_obj = Projects.objects.get(project_id=p_id)
    state_obj = state.objects.get(state_id=data['status'][0])

    task_obj = Tasks.objects.get(task_id=data['task_id'][0])

    task_obj.task_state = state_obj
    task_obj.task_deadline = data['time'][0]
    task_obj.task_descrip = data['detail'][0]
    task_obj.save()

    rtn = JsonResponse({"message":"modified"})
    rtn.status_code = 200
    return rtn

# @login_required(login_url='/PutTogether/')
# def change_password(response):
#     data = dict(response.POST)
#     user_obj =Users.objects.get(email=response.user.email)
#     user_obj.set_password(data['password'][0])
#     user_obj.save()
#     rtn = JsonResponse({"message":'password changed'})
#     rtn.status_code = 200
#     return  rtn

def ResetPassword(request):
    data = dict(request.POST)
    user_obj = Users.objects.get(email=data['email'][0])
    user_obj.set_password(data['password'][0])
    user_obj.save()
    print data['code'][0]
    for obj in PasswordCodes.objects.filter(usr_email=user_obj):
        print obj.code,obj.usr_email

    codeObjct  = PasswordCodes.objects.get(usr_email=user_obj,code=data['code'][0])
    codeObjct.isUsed = True
    codeObjct.save()
    rtn = JsonResponse({"message":'password changed'})
    rtn.status_code = 200
    return  rtn

@login_required(login_url='/PutTogether/')
def move_task(request,p_id):
    """
        changing the state of the task once the task is droppen
        :param p_id project id
        :returns json response of 200
    """""
    data = dict(request.POST)
    proj_obj = Projects.objects.get(project_id=p_id)

    from_list = state.objects.get(state_name=data['from_list'][0],project_id=proj_obj)
    to_list = state.objects.get(state_name=data['to_list'][0],project_id=proj_obj)

    to_list_positions = json.loads(data['to_list_positions'][0])
    from_list_positions = json.loads(data['from_list_positons'][0])

    for task_id in to_list_positions:
        taskObj = Tasks.objects.get(task_id=task_id,task_project_id=proj_obj)
        taskObj.task_state = to_list
        taskObj.task_position = to_list_positions[task_id]
        taskObj.save()

    for task_id in from_list_positions:
        taskObj = Tasks.objects.get(task_id=task_id,task_project_id=proj_obj)
        taskObj.task_state = from_list
        taskObj.task_position = from_list_positions[task_id]
        taskObj.save()


    # print data,'here positions'
    # task_obj = Tasks.objects.get(task_id=data['task_id'][0])
    # stat_obj = state.objects.get(state_name=data['to_list'][0],project_id=proj_obj)
    # # to_list_positions = json.loads(data['to_list_positions'][0])
    # # from_list_positions = json.loads(data['from_list_positons'][0])
    # # # task_obj.task_position = to_list_positions[str(task_obj.task_id)]
    # print task_obj.task_state.state_name,'old'
    # print stat_obj.state_name,'name'
    # print task_obj.task_name,'task name'
    # task_obj.task_state = stat_obj
    # task_obj.save()
    # print task_obj.task_state.state_name,'check'

    # for o_task in from_list_positions:
    #     obj = Tasks.objects.get(task_id=int(o_task))
    #     obj.task_position = from_list_positions[o_task]
    #     obj.save()
    #
    # for n_task in to_list_positions:
    #     if n_task != data['task_id'][0]:
    #         obj = Tasks.objects.get(task_id=int(n_task))
    #         obj.task_position = to_list_positions[n_task]
    #         obj.save()


    rtn = JsonResponse({"Saved":"New state for the task with id "+str(data['task_id'][0])})
    rtn.status_code = 200
    return rtn


def page_Home(response):
    for usr in Users.objects.all():
        print usr.email
    return render(response,'index.html')

@login_required(login_url='/PutTogether/')
def fun_new_state(request,p_id):
    """:arg
        p_id: project id
       :returns
       json response: 200 status code if the process succeeds
                     404 status code if the process fails
    """
    data = dict(request.POST)
    proj_obj = Projects.objects.get(project_id=p_id)

    response = JsonResponse({"message":''})
    if state.objects.filter(state_name=data['name'][0],project_id=proj_obj).exists():
        response = JsonResponse({"message": 'The name already exists'})
        response.status_code = 404
        return  response

    new_list = state(state_name=data['name'][0],project_id=proj_obj,state_color=data['color'][0])
    new_list.save()
    response.status_code = 200
    return response








@login_required(login_url='/PutTogether/')
def change_password(response):
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


"""Plan upgrade, Downgrade"""
@login_required(login_url='/PutTogether/')
def upgrade_account(request):
    """
     HAS SOME BUGS, WAITING FOR PROJECTS PAGE
    :param request:
    :return:
    """""
    data = dict(request.POST)
    usrObj = Users.objects.get(email=request.user)
    usrObj.account_type = data['account_type'][0]
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

""""""





"""Projects functions"""
@login_required(login_url='/PutTogether/')
def func_create_project(request):
    """
        creates a project with default lists
    :param request:
    :return: json response of 200
    """""
    data = dict(request.POST)
    usrObj= Users.objects.get(email=request.user.email)
    print usrObj,'herer chekcing'
    project = Projects(usr_email=usrObj,project_name=data['p_name'][0])
    project.save()

    # Default lists
    to_do_list = state(state_name='To Do',project_id=project)
    doing_list = state(state_name='Doing',project_id=project)
    done_list = state(state_name='Done',project_id=project)

    to_do_list.save()
    doing_list.save()
    done_list.save()

    rtn  = JsonResponse({'message':"created","project_id" :project.project_id})
    rtn.status_code = 200
    return  rtn

def func_login(request):
    data = dict(request.POST)
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
        rtn.status_code = 400
        return rtn

    else:
        new_usr = Users.objects.create_user(username=data['name'][0],password=data['pass'][0],email=data['mail'][0])
        new_usr.account_type = data['acc_type'][0]
        new_usr.save()
        login(request,new_usr)
        rtn = JsonResponse({"message":"Success"})
        rtn.status_code = 200
        return rtn

@login_required(login_url='/PutTogether/')
def func_delete_account(request):
    data = dict(request.POST)
    print request.user.email
    usr = authenticate(email=request.user.email, password=data['password'][0])
    if usr:
        usr_obj = Users.objects.get(email=usr)
        logout(request)
        usr_obj.delete()
        rtn = JsonResponse({"success":"user is deleted"})
        rtn.status_code = 200
        return rtn
    else:
        rtn = JsonResponse({"reason":"Incorrect password"})
        rtn.status_code = 400
        return rtn

@login_required(login_url='/PutTogether/')
def page_Projects(response, p_id):
    proj_obj = Projects.objects.get(project_id=p_id)
    usr_obj = Users.objects.all()[0]
    stat = state.objects.filter(state_name='new list', project_id=proj_obj)

    tasks = Tasks.objects.filter(task_project_id=proj_obj).order_by('task_position')
    states = state.objects.filter(project_id=proj_obj)
    users = Users.objects.all()

    return render(response, 'project.html', {"tasks": tasks, 'states': states, "users": users})

@login_required(login_url='/PutTogether/')
def page_User(response):

    return render(response,'user.html')



@login_required(login_url='/PutTogether/')
def display_projects(response):
    usrobj = Users.objects.get(email=response.user)
    proj = Projects.objects.filter(usr_email=usrobj)
    # for i in proj:
    #     print i.creation_time

    allow = True
    if (usrobj.account_type == 'F' and len(proj) == 5):
        allow = False
    elif (usrobj.account_type == 'P' and len(proj) == 200):
        allow = False
    elif usrobj.account_type == 'B':
        allow = True

    return render(response,'projects_page.html',{"projects":proj,'allow':allow})


@login_required(login_url='/PutTogether/')
def change_project_details(request):
    data = dict(request.POST)
    print data
    proj_obj = Projects.objects.get(project_id=data['project_id'][0])
    print proj_obj
    proj_obj.project_name=data['title'][0]
    print proj_obj.project_name
    proj_obj.save()

    # proj_obj = Projects.objects.get(project_id=p_id)
    # state_obj = state.objects.get(state_id=data['status'][0])
    #
    # task_obj = Tasks.objects.get(task_id=data['task_id'][0])
    #
    # task_obj.task_state = state_obj
    # task_obj.task_deadline = data['time'][0]
    # task_obj.task_descrip = data['detail'][0]
    # task_obj.save()

    rtn = JsonResponse({"message":"modified"})
    rtn.status_code = 200
    return rtn

@login_required(login_url='/PutTogether/')
def func_delete_project(response):
    data = dict(response.POST)
    proj_obj = Projects.objects.get(project_id=data['project_id'][0])
    proj_obj.delete()

    response = JsonResponse({"message":"project has been deleted"})
    response.status_code = 200
    return response

# def send_invite_email(response):
#     data=dict(response.POST)
#     # email=data['email'][0]
#     # print email
#     # send_mail('helloo','hel','puttogether.zenvector@gmail.com',[email],fail_silently=False)
#
#
#     send_mail('Hello from Puttogether','User invites you message','puttogether.zenvector@gmail.com',['tehadic996@email1.pro'],fail_silently=False)
#
#     response = JsonResponse({"message":"mail is sent"})
#     response.status_code = 200
#     return response

""""""





@login_required(login_url='/PutTogether/')
def func_delete_account(request):
    data = dict(request.POST)
    usr = authenticate(email=request.user.email, password=data['password'][0])
    if usr:
        usr_obj = Users.objects.get(email=usr)
        logout(request)
        usr_obj.delete()
        rtn = JsonResponse({"success":"user is deleted"})
        rtn.status_code = 200
        return rtn
    else:
        rtn = JsonResponse({"reason":"Incorrect password"})
        rtn.status_code = 400
        return rtn



@login_required(login_url='/PutTogether/')
def page_User(response):
    """
    NOT USED ANY MORE
    :param response:
    :return:
    """""
    return render(response,'user.html')


def Email_SendServer(message,toUser):

    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('puttogethersoftware@gmail.com', 'PutTogether123')

    mailserver.sendmail('puttogethersoftware@gmail.com',
                        toUser,
                        message)


"""EMAIL MESSAGES"""
def Email_SignUp(userEmail,name,accountType):
    msg = MIMEMultipart()
    msg['From'] = 'PutTogether Team'
    msg['To'] = userEmail
    msg['Subject'] = "Welcome to the PutTogether community!"
    if accountType == "F":
        features = "You are registered with the <b>free</b> version, You will be able to create 5 projects only with 5 team members at max.\n" \
                   "You can upgrade your account any time to unleash your ability."
    elif accountType == 'P':
        features = "You are registered with the <b>Premium</b> version, You will be able to create 200 projects with 50 team members at max.\n" \
                   "You can upgrade your account any time to unleash your ability."
    else:
        features = "You are registered with the <b>Platinium</b> version, You will be able to create 1000 projects with 100 team members at max.\n" \
                   "Thank you for your trust."
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <strong style="color: black">Hello <b>{name}</b></strong>
                        <p style="color: black;">Welcome to PutTogether.</p>
                        <p>{features}</p>
                        <p>Thank you for creating a PutTogether account.</p>
                        <p>For any question please contact <strong>PutTogetherSoftware@gmail.com</strong>.</p>
                        <p>PutTogether Team.</p>
                        </div>
                    </div>
                </body>
              """.format(name=name,features = features)
    msg.attach(MIMEText(message, 'html'))
    return msg.as_string()

def Email_PasswordResetCode(usrEmail,code):
    msg = MIMEMultipart()
    msg['From'] = 'PutTogether Team'
    msg['To'] = usrEmail
    msg['Subject'] = "Password Reset Code"
    message = """
                <!DOCTYPE html>
                    <html>
                    <body style="padding-top: 20px; background-color: #f5f5f5;">

                    <div style="width:500px; margin: auto; background-color: white; border-radius: 5px; border-color: #59A61E; border-style: solid;">
                        <div style="text-align: center; color: white; background-color: #59A61E">
                        <img style="align-items: ;" src="https://res.cloudinary.com/di6zpszmk/image/upload/v1575834908/puttogether1-03_xzhhab.png" width="150" height="100">
                        </div>
                        <div style="padding: 20px; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
                        <strong style="color: black">Hello </strong>
                        <p style="color: black;">You have requested to reset your account's password. </p>
                        <p>Please use the following code in the resetting process <b>{code}</b>.</p>
                        <p>For any question please contact <strong>PutTogetherSoftware@gmail.com</strong>.</p>
                        <a href="http://127.0.0.1:8000/PutTogether/PasswordResetOut/{email}/{code}">click here</a>
                        <p>PutTogether Team.</p>
                        </div>
                    </div>
                </body>
              """.format(code=code,email=usrEmail)
    msg.attach(MIMEText(message, 'html'))

    return msg.as_string()



def passwordRestOut(response,email,code):
    """
    NOT USED, FUTURE USE
    :param response:
    :return:
    """""

    code_object = PasswordCodes.objects.filter(usr_email=email,code=code)
    if len(code_object) != 0:
        return render(response,'index.html',{'Available':True,'check':code_object[0].isUsed})

    print email,code
    return render(response,'index.html',{"Available":False})
