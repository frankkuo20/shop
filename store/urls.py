from django.urls import path

from store import views


app_name = 'store'
urlpatterns = [
    path('category/', views.category, name='category'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate')
]