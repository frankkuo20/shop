from django.urls import path, re_path

from main import views

urlpatterns = [
    re_path('^.*', views.main, name='main')
]
