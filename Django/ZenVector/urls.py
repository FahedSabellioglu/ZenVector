from django.conf.urls import url
from ZenVector import views


# url(r'^pay/summary/(?P<value>\d+)/$', views.pay_summary, name='pay_summary')
urlpatterns = [
    url(r'^PutTogether/$',views.page_Home),
    url(r'^PutTogether/Projects/$',views.page_Projects),
    url(r'^PutTogether/Signup/$',views.func_signup),
    url(r'^PutTogether/User/$',views.page_User),
    url(r'^PutTogether/Login/$',views.func_login),
    url(r"^PutTogether/CreateProject/$",views.func_create_project),
    url(r'^PutTogether/Loguout/$',views.func_logout),
    url(r'^PutTogether/(?P<p_id>\d+)/NewTask/$',views.func_new_task,name='project_tasks')


]
#
# url(r'^Projects/')