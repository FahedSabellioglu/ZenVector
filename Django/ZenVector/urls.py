from django.conf.urls import url
from ZenVector import views


# url(r'^pay/summary/(?P<value>\d+)/$', views.pay_summary, name='pay_summary')
urlpatterns = [
    url(r'^PutTogether/$',views.page_Home),
    url(r'^PutTogether/Projects/$', views.display_projects),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/$',views.page_Projects,name='tasks'),
    url(r'^PutTogether/Signup/$',views.func_signup),
    url(r'^PutTogether/User/$',views.page_User),
    url(r'^PutTogether/Login/$',views.func_login),
    url(r'^PutTogether/Projects/CreateProject/$',views.func_create_project),
    url(r'^PutTogether/Loguout/$',views.func_logout),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewState/$',views.fun_new_state,name='project_tasks'),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewTask/$',views.fun_new_task),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/DeleteTask/$',views.func_delete_task),
    url(r'^PutTogether/Projects/DeleteProject/$', views.func_delete_project),
    url(r'^PutTogether/PasswordChange/$', views.change_password),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/MoveTask/$', views.move_task),
    url(r'^PutTogether/DeleteAccount/$', views.func_delete_account),
    url(r"^PutTogether/Projects/(?P<p_id>\d+)/ChangeTaskDetails/",views.change_task_details),
    url(r"^PutTogether/Projects/ChangeProjectDetails/",views.change_project_details),
    url(r"^PutTogether/Upgrade/", views.upgrade_account),
    url(r"^PutTogether/PlanBuy/", views.plan_register),
    url(r"^PutTogether/DownGrade/", views.plan_downgrade),
    url(r"^PutTogether/forgotPass/", views.forgot_pass),
    url(r"^PutTogether/CheckCode/", views.CodeChecker),
    url(r"^PutTogether/PasswordReset/", views.ResetPassword),
    url(r"^PutTogether/PasswordResetOut/(?P<email>[\w\.-]+@[\w\.-]+(\.[\w]+)+)/(?P<code>\w+)$", views.passwordRestOut),
    url(r"^PutTogether/PasswordReset/", views.ResetPassword),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/ChangeTaskDetails/',views.change_task_details),
    url(r"^PutTogether/Projects/ChangeProjectDetails/$",views.change_project_details)
    # url(r'^PutTogether/Projects/sendEmail/$', views.send_invite_email),
]
#
# url(r'^Projects/')
