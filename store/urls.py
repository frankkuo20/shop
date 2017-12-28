from django.urls import path

from store import views

urlpatterns = [
    path('category/', views.category)
]