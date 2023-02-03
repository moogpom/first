from django.urls import path
from .views import *

urlpatterns = [
   path('detailPage/<str:postId>',detail,name="detailPage"),
   path('newPost/',new,name="newPost"),
   path('editPost/<str:postId>',edit,name="editPost"),
   path('deletePost/<str:postId>',delete,name="deletePost"),
   path('photo',photo,name="photo"),
   
   path('addBookmark/<str:postId>', addBookmark,name='addBookmark'),
   path('deleteBookmark/<str:bookmarkId>', deleteBookmark,name='deleteBookmark'),
]