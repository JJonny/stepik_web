from django.conf.urls import url
from . import views

app_name = 'qa'

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^home/', views.listing, name='listing'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^question/(?P<id>\d+/?)/', views.question, name='question'),
    url(r'^ask/$', views.new_ask, name='ask'),
    url(r'^popular/', views.popular, name='popular'),
    url(r'^new/', views.test, name='new'),
    url(r'^auth_logout/', views.auth_logout, name='auth_logout'),
    url(r'^about/', views.about, name='about'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^ajax/rating_up/$', views.rating_up, name='rating_up'),
]
