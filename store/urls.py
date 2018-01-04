from django.urls import path

from store import views


app_name = 'store'
urlpatterns = [
    path('category/', views.category, name='category'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),
    path('categoryRead/<int:id>/', views.categoryRead, name='categoryRead'),
    path('categoryUpdate/<int:id>/', views.categoryUpdate, name='categoryUpdate'),
    path('categoryDelete/<int:id>/', views.categoryDelete, name='categoryDelete'),

    path('itemCreate/', views.itemCreate, name='itemCreate'),

]