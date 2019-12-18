from django import template
from ZenVector.models import *
register = template.Library()
@register.simple_tag
def progressbar(context):
    done=0
    progress=0
    proj=Projects.objects.get(project_id=context)
    tasks=Tasks.objects.filter(task_project_id=proj)

    task_user_count = len(UsrProjects.objects.filter(project_id=proj))+1

    if len(tasks) == 0:
        per = 0

    else:
        for t in tasks:
            if t.task_state.state_name=='Done':
                done+=1.0
            else:
                progress+=1.0
        per= int(done/(progress+done)*100)

    return {'percentage':per,'total':int(progress+done),'user_count':task_user_count}

