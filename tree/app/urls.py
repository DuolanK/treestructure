from django.urls import re_path
from .import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'properties', views.properties, name='properties')
]