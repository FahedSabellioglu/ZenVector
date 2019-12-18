from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ZenVector.models import *


@login_required(login_url='/PutTogether/')
def func_delete_list(response,p_id):
    """:param
        p_id: project id
        :returns
        json response of 200(succeed) status code
    """
    data = dict(response.POST)
    proj_obj = Projects.objects.get(project_id=p_id)
    stat=state.objects.get(state_id=data['list_id'][0])
    task_obj = Tasks.objects.filter(task_project_id=proj_obj,task_state=stat)

    for i in task_obj:
        i.delete()
    stat.delete()

    response = JsonResponse({"message":"task has been deleted"})
    response.status_code = 200
    return response


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