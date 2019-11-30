from django import template
from ZenVector.models import  *
register = template.Library()
@register.simple_tag
def dynamic_project_list(context):
    usr_obj = Users.objects.get(email=context)
    project_list = Projects.objects.filter(usr_email=usr_obj)
    if usr_obj.account_type == 'F' and len(project_list) == 5:
        return {
            'project_list': project_list, 'Allow':False
        }

    elif usr_obj.account_type == "P" and len(project_list) == 200:
        return {
            'project_list': project_list, 'Allow':False
        }
    elif usr_obj.account_type == "B" and len(project_list) == 1000:
        return {
            'project_list': project_list, 'Allow':False
        }

    return {
        'project_list' : project_list,'Allow':True
    }







