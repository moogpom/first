from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
   blogInfo = Blog.objects.all()
   return render(request,'home.html',{'blogInfo':blogInfo})

def detail(request,id):
   ''' blog=Blog.objects.get(id=id)'''
   blog_detail=get_object_or_404(Blog,pk=id)
   return render(request,'detail.html',{'b_detail':blog_detail})