from django.conf.urls import url
from django.http import HttpResponse
from company import views

urlpatterns = [
    url(r'^accueil$', views.home),
    url(r'^(\d+)$', views.view_company), 
    url(r'^date$', views.date_actuelle),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]