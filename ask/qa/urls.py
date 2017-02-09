from django.conf.urls import url
from . import views


app_name = 'qa'

urlpatterns = [
   url(r'^$', views.test, name='index'),
   url(r'^login/', views.test, name='login'),
   url(r'^singup/', views.test, name='singup'),
   url(r'^question/', views.test, name='question'),
   url(r'^ask/', views.test, name='ask'),
   url(r'^popular/', views.test, name='popular'),
   url(r'^new/', views.test, name='new'),
]