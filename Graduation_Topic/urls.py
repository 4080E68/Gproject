from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp import views

urlpatterns = [
    url('^callback', views.callback),
    
    url('^$', views.index),
    url('^chassis/$', views.Chassis),
    url('^cpu/$', views.CPU),
    url('^hdd/$', views.HDD),
    url('^ssd/$', views.SSD),
    url('^login/$', views.Login),
    url('^aftlogin/$', views.aftlogin),
    url('^signup/$', views.Signup),
    url('^MB/$', views.MB1),
    url('^Memory/$', views.Memory1),
    url('^Power/$', views.Power1),
    url('^display/$', views.Display),
    url('^otcpu/$', views.otcpu),
    url('^otchassis/$', views.otchassis),
    url('^otdisplay/$', views.otdisplay),
    url('^othdd/$', views.othdd),
    url('^otMB/$', views.otMB),
    url('^otPower/$', views.otPower),
    url('^otssd/$', views.otssd),
    url('^otMemory/$', views.otMemory),
    url('^cart/$', views.CART),
    path('bind/<str:key>/', views.bind),
    path('admin/', admin.site.urls),
]
