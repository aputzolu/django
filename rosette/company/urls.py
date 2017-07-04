from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import ListView
from company import views
from .models import Company

urlpatterns = [
    url(r'^$', views.CompanyList.as_view(), name="company_list"),  
    # url(r'^$', ListView.as_view(model=Company,
    #                 context_object_name="companies",
    #                 template_name="company/accueil.html")),

    # url(r'^$', views.accueil, name='accueil'),
    url(r'^(\d+)$', views.lire, name='lire'),
    url(r'^(\d+)/user/(\d+)$', views.user, name='user'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^company/$', views.company, name='company'),
    url(r'^user/$', views.addUser, name='user'),
    # url(r'^(\d+)$', views.view_company), 
    # url(r'^date$', views.date_actuelle),
    # url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
]