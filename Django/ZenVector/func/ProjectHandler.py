from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ZenVector.models import *
from django.core import serializers



@login_required(login_url='/PutTogether/')
def CreateProject(request):
    """
        creates a project with default lists
    :param request:
    :return: json response of 200
    """""
    data = dict(request.POST)
    usrObj= Users.objects.get(email=request.user.email)
    project = Projects(usr_email=usrObj,project_name=data['p_name'][0])
    project.save()

    # Default lists
    # to_do_list = state(state_name='To Do',project_id=project)
    # doing_list = state(state_name='Doing',project_id=project)
    # done_list = state(state_name='Done',project_id=project)
    #
    # to_do_list.save()
    # doing_list.save()
    # done_list.save()


    # to_do_default = Tasks(task_name="Default Task To Do",task_project_id=project,task_descrip ="Default Task",
    #                  task_given_by = project.usr_email,task_state=to_do_list,task_deadline="2019-02-09",
    #                  task_position=0)
    # doing_default = Tasks(task_name="Default Task Doing",task_project_id=project,task_descrip ="Default Task",
    #                  task_given_by = project.usr_email,task_state=doing_list,task_deadline="2019-02-09",
    #                  task_position=0)
    # done_default = Tasks(task_name="Default Task Done",task_project_id=project,task_descrip ="Default Task",
    #                  task_given_by = project.usr_email,task_state=done_list,task_deadline="2019-02-09",
    #                  task_position=0)
    #
    # to_do_default.save()
    # doing_default.save()
    # done_default.save()

    rtn  = JsonResponse({'message':"created","project_id" :project.project_id})
    rtn.status_code = 200
    return  rtn

@login_required(login_url='/PutTogether/')
def InviteMembers(response):
    data = dict(response.POST)
    users = map(lambda x:x.strip(),data['users'][0].split(','))
    project_obj = Projects.objects.get(project_id=data['project_id'][0])
    proj_users = [user.usr_email for user in UsrProjects.objects.filter(project_id=project_obj)]
    delete_proj_users = [userobj for userobj in proj_users if userobj.email not in users]

    print len(UsrProjects.objects.filter(project_id=project_obj)),'old'
    for userobj in delete_proj_users:
        proj_usr = UsrProjects.objects.filter(usr_email=userobj)
        proj_usr.delete()
        print "DELETE USER"


    print len(UsrProjects.objects.filter(project_id=project_obj)),'new'

    for user in users:
        if len(Users.objects.filter(email=str(user))) != 0:
            userObj = Users.objects.get(email=str(user))
            if userObj not in proj_users:
                if len(UsrProjects.objects.filter(project_id=project_obj)) == 5:
                    rtn = JsonResponse({"message": "Not Allow"})
                    rtn.status_code = 200
                    return rtn
                usrProjObj = UsrProjects(usr_email=userObj,project_id=project_obj)
                usrProjObj.save()
                print "NEW USER TO PROJECT"

        else:
            print "NEW USER TO APP"
            #TODO NEW USER

    rtn = JsonResponse({"message": "added"})
    rtn.status_code = 200
    return rtn

@login_required(login_url='/PutTogether/')
def ChangeProjectDetails(request):
    data = dict(request.POST)
    proj_obj = Projects.objects.get(project_id=data['project_id'][0])
    proj_obj.project_name=data['title'][0]
    proj_obj.save()

    rtn = JsonResponse({"message":"modified"})
    rtn.status_code = 200
    return rtn

@login_required(login_url='/PutTogether/')
def DeleteProject(response):
    data = dict(response.POST)
    print data,'data'
    proj_obj = Projects.objects.get(project_id=data['project_id'][0])
    proj_obj.delete()

    response = JsonResponse({"message":"project has been deleted"})
    response.status_code = 200
    return response

@login_required(login_url='/PutTogether/')
def GetProjectMembers(request):
    project_ID = dict(request.GET)['project_id'][0]
    user_projects = UsrProjects.objects.filter(project_id=Projects.objects.get(project_id=project_ID))
    serialized_qs = serializers.serialize('json', list(user_projects))
    rtn = JsonResponse({"message": "added",'users':serialized_qs})
    rtn.status_code = 200
    return rtn