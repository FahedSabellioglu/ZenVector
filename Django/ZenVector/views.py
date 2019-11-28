# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.contrib.auth import login,logout,authenticate
from models import *
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/PutTogether/')
def fun_new_state(request,p_id):
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
def fun_new_task(response,p_id):
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
    data = dict(response.POST)
    proj_obj = Projects.objects.get(project_id=p_id)
    task_obj = Tasks.objects.get(task_id=data['taskid'][0],task_project_id=proj_obj)
    task_obj.delete()

    response = JsonResponse({"message":"task has been deleted"})
    response.status_code = 200
    return response

@login_required(login_url='/PutTogether/')
def change_task_details(request,p_id):
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

@login_required(login_url='/PutTogether/')
def change_password(response):
    data = dict(response.POST)
    user_obj =Users.objects.get(email=response.user.email)
    user_obj.set_password(data['password'][0])

    rtn = JsonResponse({"message":'password changed'})
    rtn.status_code = 200
    return  rtn


@login_required(login_url='/PutTogether/')
def move_task(request,p_id):
    data = dict(request.POST)
    proj_obj = Projects.objects.get(project_id=p_id)
    task_obj = Tasks.objects.get(task_id=data['task_id'][0])
    stat_obj = state.objects.get(state_name=data['to_list'][0],project_id=proj_obj)
    task_obj.task_state = stat_obj
    task_obj.save()

    rtn = JsonResponse({"Saved":"New state for the task with id "+str(data['task_id'][0])})
    rtn.status_code = 200
    return rtn


def page_Home(response):

    return render(response,'index.html')


@login_required(login_url='/PutTogether/')
def func_logout(request):

    logout(request)
    return HttpResponseRedirect('/PutTogether/')


@login_required(login_url='/PutTogether/')
def func_create_project(request):
    data = dict(request.POST)
    usrObj= Users.objects.get(email=request.user.email)
    print usrObj
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
        rtn.status_code = 400
        return rtn

    else:
        new_usr = Users.objects.create_user(username=data['name'][0],password=data['pass'][0],email=data['mail'][0])
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
def page_Projects(response,p_id):
    proj_obj = Projects.objects.get(project_id=p_id)
    usr_obj = Users.objects.all()[0]
    stat = state.objects.filter(state_name='new list',project_id=proj_obj)

    tasks = Tasks.objects.filter(task_project_id=proj_obj)
    states = state.objects.filter(project_id=proj_obj)
    users= Users.objects.all()


    return render(response,'project.html',{"tasks":tasks,'states':states ,"users":users})

@login_required(login_url='/PutTogether/')
def page_User(response):

    return render(response,'user.html')


@login_required(login_url='/PutTogether/')
def display_projects(response):

    logged_in=response.user
    # print response.user
    # proj= Projects.objects.get(project_id=64)
    # proj.delete()

    proj = Projects.objects.filter(usr_email=logged_in)
    print proj

    return render(response,'projects_page.html',{"projects":proj})


@login_required(login_url='/PutTogether/')
def change_project_details(request,p_id):
    data = dict(request.POST)

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
    proj_obj = Projects.objects.get(project_id=p_id)
    proj_obj.delete()

    response = JsonResponse({"message":"project has been deleted"})
    response.status_code = 200
    return response




# Create your views here.
