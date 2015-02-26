from leialater import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'), 
    url(r'^dashboard/$', views.dashboard, name='dasbhoard'),   
    url(r'^register/$', views.register, name='register'),      
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_url/$', views.add_url, name = 'add_url'),
   )

