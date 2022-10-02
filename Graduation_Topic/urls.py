from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import include, re_path

urlpatterns = [
    re_path('^callback', views.callback),
    re_path('^$', views.index),
    re_path('^chassis/$', views.Chassis),
    re_path('^cpu/$', views.CPU),
    re_path('^hdd/$', views.HDD),
    re_path('^ssd/$', views.SSD),
    re_path('^login/$', views.Login),
    re_path('^adminLogout/$', views.adminLogout),
    re_path('^aftlogin/$', views.aftlogin),
    re_path('^signup/$', views.Signup),
    re_path('^MB/$', views.MB1),
    re_path('^Memory/$', views.Memory1),
    re_path('^Power/$', views.Power1),
    re_path('^display/$', views.Display),
    re_path('^otcpu/$', views.otcpu),
    re_path('^otchassis/$', views.otchassis),
    re_path('^otdisplay/$', views.otdisplay),
    re_path('^othdd/$', views.othdd),
    re_path('^otMB/$', views.otMB),
    re_path('^otPower/$', views.otPower),
    re_path('^otssd/$', views.otssd),
    re_path('^otMemory/$', views.otMemory),
    re_path('^cart/$', views.CART),
    re_path('^form/$', views.form),
    re_path('^manager/$', views.manager),
    path('update/<str:table>/<str:key>/', views.update),
    path('bind/<str:key>/', views.bind),
    path('admin/', admin.site.urls),
]
