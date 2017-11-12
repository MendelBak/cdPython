from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.process_form),
    url(r'^result$', views.result),
    url(r'^go_back$', views.go_back),
    url(r'^clear_counter$', views.clear_counter),
]