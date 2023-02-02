from django.contrib import admin
from .models import PomBlog
# Register your models here.

admin.site.register(PomBlog)

def __str__(self):
 return self.title