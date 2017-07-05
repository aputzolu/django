from django.conf.urls import url
from django.http import HttpResponse
from user import views

urlpatterns = [
    url(r'^signup/$', views.addUser, name='signup'),
    url(r'^$', views.UserList.as_view(), name="user_list"),
    url(r'^(\d+)$', views.user, name='userprofile'),
]