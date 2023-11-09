from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= 'list_page'),
    path('update/<str:pk>/', updateTask, name= 'update_page'),
    path('delete/<str:pk>/', deleteTask, name= 'delete_page'),
]
