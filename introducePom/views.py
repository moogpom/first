from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import PomBlog

# Create your views here.

def home(request):
    blogs=PomBlog.objects.all()
    return render(request,"home.html",{'blogContents':blogs})

def detailPost(request,postId):
    post=get_object_or_404(PomBlog,pk=postId)
    return  render(request,'detailPost.html',{'postContents':post})

def newPost(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때 method가 post다
        createPost=PomBlog()
        createPost.title=request.POST['title']
        createPost.writer=request.POST['writer']
        createPost.body=request.POST['body']
        #createPost.image = request.FILES['image']
        #사진을 올리지 않았을 때 기본이미지가 들어가도록함
        #if request.FILES.get('image') is not None:
        createPost.image = request.FILES.get('image')
        createPost.pub_date=timezone.now()
        createPost.save()
        return redirect("detailPost",createPost.id)
    else :#글 작성 후 저장버튼 눌렀을 때 method가 post가 아니다->
        #맨처음 새글작성버튼 눌렀을 때 newPost페이지 뜨게함
        return render(request,"newPost.html")

def edit(request,postId):
    #updatePost=PomBlog.objects.get(id=postId)
    updatePost = get_object_or_404(PomBlog,pk=postId)
    if request.method == 'POST': #글 수정 후 저장버튼 눌렀을 때 method가 post다
        updatePost.title=request.POST['title']
        updatePost.writer=request.POST['writer']
        updatePost.body=request.POST['body']
        #updatePost.image = request.FILES['image']
        if request.FILES.get('image') is not None:
           updatePost.image = request.FILES.get('image')
        updatePost.pub_date=timezone.now()
        updatePost.save()
        return redirect("detailPost",updatePost.id)
    else :# method가 post가 아니다-> get이다
         #맨처음 수정버튼 눌렀을 때 editPost페이지 뜨게함
        return render(request,"editPost.html",{'postContents':updatePost})

def delete(request,postId):
    deleteBook = get_object_or_404(PomBlog,pk=postId)
    deleteBook.delete()
    return redirect('home')

