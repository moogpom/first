from django.urls import path
from .views import *

urlpatterns = [
   path('howToGo',howToGo,name="howToGo"),
   path('sonjjangnan',sonjjangnan,name="sonjjangnan"),
   path('introClass',introClass,name="introClass"),
]