from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^manager/$', views.manager, name='manager'),
    url(r'^validate/$', views.manager, name='validate'),
    url(r'^(?P<user_id>user[0-9]+)/(?P<serial>[0-9]+)/(?P<input_file>[\w,\s-]+\.gcode)/$', views.bioprint, name='bioprint'),
    url(r'^(?P<user_id>user[0-9]+)/$', views.user, name='user'),
]
