from django.urls import path, re_path

from main import views

app_name = 'main'
urlpatterns = [
    path('', views.main, name='main')
    # re_path('^.*', views.main, name='main')
]
