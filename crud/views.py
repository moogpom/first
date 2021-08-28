
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone
from .forms import  *
from django.views.generic.edit import FormView
from django.db.models import Q
from django.core.paginator import Paginator


def photo(request):
    allPost= Photo.objects.all().order_by('-id')
    paginatorPost = Paginator(allPost, 3)
    page = request.GET.get('page')
    posts = paginatorPost.get_page(page)
    return render(request,"photo.html",{'photoList':allPost, 'posts': posts})

#상세창
def detail(request,postId):
    post = get_object_or_404(Photo,pk=postId) 
    bookmarkForm =BookmarkForm()
    return  render(request,'detail.html',{'postContents':post,'bookmarkForm':bookmarkForm })

#새로운 글 작성
def new(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        post_form =  PhotoForm(request.POST,request.FILES)
        if post_form.is_valid():# 이 form을 유효한지 검사후 유효하면 save해줌 (임시저장)
            post = post_form.save(commit = False)#임시저장 해주는 이유는 model에 있는 필드 중 new date를 안 담았음 (commit=False)
            post.pub_date = timezone.now() 
            post.writer = request.user
            post.save()
            return redirect("detailPage",post.id)
    else:
        post_form =  PhotoForm()
        return render(request,'new.html',{'post_form':post_form})
 
#수정
def edit(request,postId):
    post = get_object_or_404(Photo,pk=postId)
    if request.method == 'GET': #수정
        post_form=PhotoForm(instance=post)
        return render(request,'edit.html',{'post_form': post_form})
    else:
        post_form = PhotoForm(request.POST,request.FILES,instance = post)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.pub_date = timezone.now() # 날짜 생성
            post.writer = request.user
            post.save()
        return redirect("detailPage",post.id)

#게시글 삭제
def delete(request,postId):
   deletePost = get_object_or_404(Photo,pk=postId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('photo')

def deleteBookmark(request,bookmarkId):
   deletePost = get_object_or_404(Bookmark,pk=bookmarkId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('photo')

def addBookmark(request, postId):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        book_form =  BookmarkForm(request.POST)
        if book_form.is_valid():# 이 form을 유효한지 검사후 유효하면 save해줌 (임시저장)
            book = book_form.save(commit = False)#임시저장 해주는 이유는 model에 있는 필드 중 new date를 안 담았음 (commit=False)
            book.postId = Photo.objects.get(pk = postId)
            print(book.postId.id)
            book.userId = request.user
            print("북마트추가")
            book.save()
            return redirect("detailPage", postId)

