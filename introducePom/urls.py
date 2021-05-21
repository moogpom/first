from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detailPost/<str:postId>',detailPost,name="detailPost"),
    path('newPost/',newPost,name="newPost"),
    path('editPost/<str:postId>',edit,name="editPost"),
    path('deletePost/<str:postId>',delete,name="deletePost"),
    path('deleteimage/<str:postId>',deleteimage,name="deleteimage"),
    path('deleteAll',deleteAll,name="deleteAll"),
]