from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:bookId>',detailPage,name="detailBook"),
    path('newBook/',newPage,name="newBook"),
    path('editBook/<str:bookId>',edit,name="editBook"),
    path('deleteBook/<str:bookId>',delete,name="deleteBook"),
]