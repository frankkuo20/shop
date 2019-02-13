from django.urls import path

from userAuth import views

app_name = 'userAuth'
urlpatterns = [
    path('userLogin/', views.userLogin, name='userLogin'),
    path('userLogout/', views.userLogout, name='userLogout'),
    path('register/', views.register, name='register')
]
