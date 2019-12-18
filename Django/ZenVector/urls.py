from django.conf.urls import url
from ZenVector import views

urlpatterns = [
    url(r'^PutTogether/$',views.page_Home,name='PutTogether'),
    url(r'^PutTogether/Signup/$', views.Signup,name='SignUP'),
    url(r'^PutTogether/Login/$', views.Login),
    url(r"^PutTogether/PlanBuy/", views.Signup),
    url(r'^PutTogether/Loguout/$', views.Logout),

    url(r'^PutTogether/PasswordChange/$', views.Logged_change_password),
    url(r'^PutTogether/DeleteAccount/$', views.DeleteAccount),
    url(r"^PutTogether/forgotPass/", views.RequestPasswordResetCode),
    url(r"^PutTogether/CheckCode/", views.PasswordResetCodeValidity),
    url(r"^PutTogether/PasswordReset/", views.NonLogged_ResetPassword),
    # url(r"^PutTogether/PasswordReset/", views.ResetPassword),
    url(r"^PutTogether/PasswordResetOut/(?P<email>[\w\.-]+@[\w\.-]+(\.[\w]+)+)/(?P<code>\w+)$",views.PasswordResetLink),


    url(r'^PutTogether/Projects/CreateProject/$', views.CreateProject),
    url(r'^PutTogether/Projects/DeleteProject/$', views.DeleteProject),
    # url(r"^PutTogether/Projects/ChangeProjectDetails/", views.ChangeProjectDetails),
    url(r"^PutTogether/Projects/ChangeProjectDetails/$", views.ChangeProjectDetails),
    url(r'^PutTogether/Projects/InviteMember$', views.InviteMembers),
    url(r'^PutTogether/Projects/getMembers$', views.GetProjectMembers),

    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewTask/$', views.NewTask),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/DeleteTask/$', views.DeleteTask),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/ChangeTaskDetails/', views.ChangeTaskDetails),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/getTaskUsers/$', views.TaskMembers),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/MoveTask/$', views.MoveTask),


    url(r'^PutTogether/Projects/(?P<p_id>\d+)/NewState/$', views.NewState, name='project_tasks'),
    url(r'^PutTogether/Projects/(?P<p_id>\d+)/DeleteList/$', views.DeleteState),


    url(r"^PutTogether/Upgrade/", views.UpgradeAccount),
    url(r"^PutTogether/DownGrade/", views.DowngradeAccount),


    url(r'^PutTogether/Projects/(?P<p_id>\d+)/$', views.page_Projects, name='tasks'),
    url(r'^PutTogether/Projects/$', views.display_projects),
    url(r'^PutTogether/User/$', views.page_User),
    url(r"ContactUs/$",views.contact_us),



]

