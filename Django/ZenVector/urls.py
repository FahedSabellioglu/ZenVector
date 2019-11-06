from django.conf.urls import url
from ZenVector import views



urlpatterns = [
    url(r'^PutTogether/$',views.page_Home),
    url(r'^PutTogether/Projects/$',views.page_Projects),
    url(r'^Login/$',views.func_login),
    url(r'^PutTogether/User/$',views.page_User),


]
#
# url(r'^Projects/')