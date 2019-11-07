from django import template
from ZenVector.models import  *
register = template.Library()
@register.simple_tag
def dynamic_project_list(context):
    project_list = Projects.objects.all()

    return {
        'project_list' : project_list,
    }





