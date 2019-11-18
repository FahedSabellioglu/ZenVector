from django.conf.urls import url
from ZenVector import views


# url(r'^pay/summary/(?P<value>\d+)/$', views.pay_summary, name='pay_summary')
urlpatterns = [
    url(r'^PutTogether/$',views.page_Home),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/$',views.page_Projects,name='tasks'),
    url(r'^PutTogether/Signup/$',views.func_signup),
    url(r'^PutTogether/User/$',views.page_User),
    url(r'^PutTogether/Login/$',views.func_login),
    url(r"^PutTogether/CreateProject/$",views.func_create_project),
    url(r'^PutTogether/Loguout/$',views.func_logout),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewState/$',views.fun_new_state,name='project_tasks'),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewTask/$',views.fun_new_task),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/DeleteTask/$',views.func_delete_task),
    url(r'^PutTogether/PasswordChange/$', views.change_password)

]
#
# url(r'^Projects/')