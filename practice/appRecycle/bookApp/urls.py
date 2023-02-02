
from django.urls import path
from .views import *

urlpatterns = [
    path('detailPage/<str:bookId>',detailPage,name="detailPage"),
    path('newBook/',newPage,name="newBook"),
    path('editBook/<str:bookId>',edit,name="editBook"),
    path('deleteBook/<str:bookId>',delete,name="deleteBook"),
    path('deleteAll',deleteAll,name="deleteAll"),
]