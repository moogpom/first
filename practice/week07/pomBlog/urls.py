from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:postId>',detail,name="detail"),
    path('newPost/',new,name="newPost"),
    path('create/',create,name="create"),
    path('editPost/<str:postId>',edit,name="editPost"),
    path('updatePost/<str:postId>',update,name="updatePost"),
    path('delete/<str:postId>',delete,name="deletePost"),
]
