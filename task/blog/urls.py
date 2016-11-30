from django.conf.urls import url, include
from blog import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'heading/(?P<title>([\w ]+))$', views.heading, name='heading'),
   url(r'sub_titles/(?P<sub_title>([\w ]+))$', views.sub_titles, name='sub_titles'),
   #url(r'^new/(?P<state>([\w ]+))$', views.new_state, name='new_state'),
]
