from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^session_words$', views.session_words),
    url(r'^add_word$', views.add_word),
    url(r'^reset$', views.reset),
]