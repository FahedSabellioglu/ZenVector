from django.http import JsonResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from ZenVector.models import *
import json

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

    task_position = len(Tasks.objects.filter(task_project_id=proj_obj,task_state=state_obj))
    if task_position != 0:
        task_position += 1

    new_task = Tasks(task_name=data['title'][0],task_project_id=proj_obj,task_descrip = data['descrip'][0],
                     task_given_by = proj_obj.usr_email,task_state=state_obj,task_deadline=data['date'][0],
                     task_position=task_position)
    new_task.save()

    for user in data['assign_to'][0].strip().split(","):
        if len(Users.objects.filter(email=user.strip())) != 0:
            if len(UsrTasks.objects.filter(task_id=new_task,usr_email=Users.objects.get(email=user.strip()))) == 0:
                usrTask = UsrTasks(task_id=new_task,usr_email=Users.objects.get(email=user.strip()))
                usrTask.save()
                print "NEW USER TO TASK"
        else:
            print "NEW USER TO APP"
        print (user,'here')

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
        print taskObj.task_id,to_list_positions[task_id]
        taskObj.save()

    for task_id in from_list_positions:
        taskObj = Tasks.objects.get(task_id=task_id,task_project_id=proj_obj)
        taskObj.task_state = from_list
        taskObj.task_position = from_list_positions[task_id]
        taskObj.save()

    rtn = JsonResponse({"Saved":"New state for the task with id "+str(data['task_id'][0])})
    rtn.status_code = 200
    return rtn

@login_required(login_url='/PutTogether/')
def task_users(response,p_id):
    data = dict(response.GET)

    task_obj = Tasks.objects.get(task_id=data['taskid'][0])
    task_users =  [usrTask.usr_email for usrTask in UsrTasks.objects.filter(task_id=task_obj)]
    ser_users = serializers.serialize('json', list(task_users))
    rtn = JsonResponse({"message": "task users",'users':ser_users})
    rtn.status_code = 200

    return rtn