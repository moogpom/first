from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import PomBlog

# Create your views here.
def home(request):
    blogContents=PomBlog.objects.all()
    return render(request,'home.html',{'blogContents':blogContents})

def detail(request,postId):
    post = get_object_or_404(PomBlog,pk=postId)
    return  render(request,'detail.html',{'postContents':post})

def new(request):
    return render(request,"new.html")

def create(request):
    createPost=PomBlog()
    createPost.title=request.POST['title']
    createPost.writer=request.POST['writer']
    createPost.body=request.POST['body']
    createPost.pub_date=timezone.now()
    createPost.save()
    return redirect("detail",createPost.id)

def edit(request,postId):
    editBlog=PomBlog.objects.get(id=postId)
    return render(request,'edit.html',{'blogContents':editBlog})

def update(request,postId):
    updatePost=PomBlog.objects.get(id=postId)
    updatePost.title=request.POST['title']
    updatePost.writer=request.POST['writer']
    updatePost.body=request.POST['body']
    updatePost.pub_date=timezone.now()
    updatePost.save()
    return redirect("detail",updatePost.id)

def delete(request,postId):
    deletePost=PomBlog.objects.get(id=postId)
    deletePost.delete()
    return redirect('home')