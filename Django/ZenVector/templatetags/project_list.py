from django import template
from ZenVector.models import  *
register = template.Library()
@register.simple_tag
def dynamic_project_list(context):
    usr_obj = Users.objects.get(email=context)
    project_list = Projects.objects.filter(usr_email=usr_obj)
    return {
        'project_list' : project_list,
    }





