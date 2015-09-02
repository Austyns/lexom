from django.conf.urls import patterns, url
from law import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN! 
        url(r'^login/$', views.user_login, name='login'),
       # url(r'^profile/$', views.profile, name='profile'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        )