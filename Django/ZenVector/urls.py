from django.conf.urls import url
from ZenVector import views

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
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/DeleteList/$',views.func_delete_list),
    url(r'^PutTogether/Projects/DeleteProject/$', views.func_delete_project),
    url(r'^PutTogether/PasswordChange/$', views.change_password),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/MoveTask/$', views.move_task),
    url(r'^PutTogether/DeleteAccount/$', views.func_delete_account),
    url(r"^PutTogether/Projects/(?P<p_id>\d+)/ChangeTaskDetails/",views.change_task_details),
    url(r"^PutTogether/Projects/ChangeProjectDetails/",views.change_project_details),
    url(r"^PutTogether/Upgrade/", views.upgrade_account),
    url(r"^PutTogether/PlanBuy/", views.func_signup),
    url(r"^PutTogether/DownGrade/", views.plan_downgrade),
    url(r"^PutTogether/forgotPass/", views.forgot_pass),
    url(r"^PutTogether/CheckCode/", views.CodeChecker),
    url(r"^PutTogether/PasswordReset/", views.ResetPassword),
    url(r"^PutTogether/PasswordResetOut/(?P<email>[\w\.-]+@[\w\.-]+(\.[\w]+)+)/(?P<code>\w+)$", views.LinkCheckPassRest),
    url(r"^PutTogether/PasswordReset/", views.ResetPassword),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/ChangeTaskDetails/',views.change_task_details),
    url(r"^PutTogether/Projects/ChangeProjectDetails/$",views.change_project_details),
    url(r"ContactUs/$",views.contact_us),
    url(r'^PutTogether/Projects/InviteMember$', views.add_users),
    url(r'^PutTogether/Projects/getMembers$', views.get_users),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/getTaskUsers/$', views.task_users),

]

