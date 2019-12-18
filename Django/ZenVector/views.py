# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core import serializers
from models import *
from func.Auth import *
from func.TasksHandler import *
from func.PlansHandler import  *
from func.PasswordHandler import *
from func.ProjectHandler import  *
from func.StatesHandler import  *



def page_Home(response):
    """
        :returns Home Page
    """""
    return render(response,'index.html')

@login_required(login_url='/PutTogether/')
def page_Projects(response, p_id):
    """
        
    :param response: 
    :param p_id: Project id
    :return: the user request project page ( tasks and states )
    """""
    proj_obj = Projects.objects.get(project_id=p_id)
    proj_users = [str(usrProjobj.usr_email.email) for usrProjobj in UsrProjects.objects.filter(project_id=proj_obj)] + [str(proj_obj.usr_email.email)]
    if str(response.user) not  in proj_users:
        return render(response, '404.html')

    tasks = Tasks.objects.filter(task_project_id=proj_obj).order_by('task_position')
    states = state.objects.filter(project_id=proj_obj)
    users = [ usrObj.usr_email for usrObj in UsrProjects.objects.filter(project_id=proj_obj)]
    users.append(proj_obj.usr_email)

    return render(response, 'project.html', {"tasks": tasks, 'states': states, "users": users,'project_name':proj_obj.project_name})


@login_required(login_url='/PutTogether/')
def display_projects(response):
    """

    :param response: 
    :return: All the projects related to the user
    """""
    usrobj = Users.objects.get(email=response.user)
    proj = Projects.objects.filter(usr_email=usrobj)
    users = [user.email for user in Users.objects.exclude(email=usrobj.email)]
    allow = True
    if (usrobj.account_type == 'F' and len(proj) == 5):
        allow = False
    elif (usrobj.account_type == 'P' and len(proj) == 200):
        allow = False
    elif usrobj.account_type == 'B':
        allow = True

    all_projects = list(proj)+[p.project_id for p in UsrProjects.objects.filter(usr_email=usrobj)]

    return render(response,'projects_page.html',{"projects":all_projects,'allow':allow,'users':users})


"""THE END"""
def contact_us(response):
    """
        a handler for the user email sender 
    :param response: 
    :return:  
    """""
    data = dict(response.POST)
    message=data['message'][0]
    subject=data['subject'][0]
    if data['email'][0]=="":
        email=response.user.email
    else:
        email=data['email'][0]

        message = Email_Contact_Us(email,subject,message)
        Email_SendServer(message,'puttogethersoftware@gmail.com')

    response = JsonResponse({"message":"mail is send"})
    response.status_code = 200
    return response





"""TO BE DELETED"""

# def ResetPassword(request):
#     """"
#         changes the password of the user after passing all the checks.
#         :param
#         :returns json response of 200 status code
#     """""
#
#     data = dict(request.POST)
#     user_obj =Users.objects.get(email=data['email'][0])
#     user_obj.set_password(data['password'][0])
#     user_obj.save()
#     rtn = JsonResponse({"message":'password changed'})
#     rtn.status_code = 200
#     return  rtn
# def func_signup(request):
#     """"
#         signing up a new user, Free version only
#     :param request
#     :returns json response 400 or 200 status code
#     """""
#
#     data =  dict(request.POST)
#     print data,'gets'
#     if Users.objects.filter(email=data['mail'][0]).exists():
#         rtn = JsonResponse({"message":"Failed",'reason':"This email address is used"})
#         rtn.status_code = 403
#         return rtn
#     else:
#         print data['acc_type'][0]
#         new_usr = Users.objects.create_user(username=data['name'][0],password=data['pass'][0],email=data['mail'][0])
#         new_usr.account_type = data['acc_type'][0]
#         message  = Email_SignUp(data['mail'][0],data['name'][0],data['acc_type'][0])
#         Email_SendServer(message,data['mail'][0])
#         new_usr.save()
#         login(request,new_usr)
#         rtn = JsonResponse({"message":"Success"})
#         rtn.status_code = 200
#         return rtn
# @login_required(login_url='/PutTogether/')
# def change_password(response):
#     data = dict(response.POST)
#     user_obj =Users.objects.get(email=response.user.email)
#     user_obj.set_password(data['password'][0])
#     user_obj.save()
#     rtn = JsonResponse({"message":'password changed'})
#     rtn.status_code = 200
#     return  rtn
""""""
"""Projects functions"""
@login_required(login_url='/PutTogether/')
def page_User(response):
    return render(response,'user.html')
#
# @login_required(login_url='/PutTogether/')
# def func_delete_account(request):
#     data = dict(request.POST)
#     usr = authenticate(email=request.user.email, password=data['password'][0])
#     if usr:
#         usr_obj = Users.objects.get(email=usr)
#         logout(request)
#         usr_obj.delete()
#         rtn = JsonResponse({"success":"user is deleted"})
#         rtn.status_code = 200
#         return rtn
#     else:
#         rtn = JsonResponse({"reason":"Incorrect password"})
#         rtn.status_code = 400
#         return rtn
@login_required(login_url='/PutTogether/')
def page_User(response):
    """
    NOT USED ANY MORE
    :param response:
    :return:
    """""
    return render(response,'user.html')
"""Password Rest Functions"""






