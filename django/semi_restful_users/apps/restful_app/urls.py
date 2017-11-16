from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show/(?P<user_id>\d+)$', views.show), #The regex is a group capture field which will create a variable "user_id" and store the number passed to it by the index.html href.
    url(r'^new_user$', views.new_user), 
    url(r'^create$', views.create), 
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy), 
    url(r'^edit/(?P<user_id>\d+)$', views.edit), 
    url(r'^update_user/(?P<user_id>\d+)$', views.update_user), 
]