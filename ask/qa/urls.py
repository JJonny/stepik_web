from django.conf.urls import url
from . import views


app_name = 'qa'

urlpatterns = [
   url(r'^$', views.test, name='index'),
   url(r'^login/', views.test, name='login'),
   url(r'^signup/', views.test, name='signup'),
   url(r'^question/(?P<id>\d+/?)', views.test, name='question'),
   url(r'^ask/$', views.test, name='ask'),
   url(r'^popular/', views.test, name='popular'),
   url(r'^new/', views.test, name='new'),
   url(r'^about/', views.about, name='about'),
]
