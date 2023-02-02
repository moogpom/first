from django.core import paginator
from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

# Create your views here.
def homePage(request):
    books=Book.objects.all()
    #블로그 모든 글들을 대상으로
    book_list = Book.objects.all()
    #블로그 객체 세 개를 한페이지로 자르고
    paginator = Paginator(book_list,3)
    #request된 페이지가 뭔지를 알아내고(request 페이지를 변수로 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해준다
    bookPosts = paginator.get_page(page)
    return render(request,"homePage.html",{'bookContents':books,'bookPosts':bookPosts})

def detailPage(request,bookId):
    books=get_object_or_404(Book,pk=bookId)
    return render(request,"detailPage.html",{'bookContents':books})

def newPage(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        book_form = BookForm(request.POST,request.FILES)
        if book_form.is_valid():
            book = book_form.save(commit = False)
            book.new_date = timezone.now() # 날짜 생성
            book.save()
            return redirect("detailPage",book.id)
    else:
        book_form = BookForm()
        return render(request,'newPage.html',{'form':book_form})

def edit(request,bookId):
    book = get_object_or_404(Book,pk=bookId)
    if request.method == 'GET': #수정
        book_form=BookForm(instance=book)
        return render(request,'editPage.html',{'edit_post':book_form})
    else:
        book_form = BookForm(request.POST,request.FILES,instance = book)
        if book_form.is_valid():
            book = book_form.save(commit = False)
            book.new_date = timezone.now() # 날짜 생성
            book.save()
        return redirect("detailPage",book.id)

    

def delete(request,bookId):
    deleteBook=Book.objects.get(id=bookId)
    deleteBook.delete()
    return redirect('homePage')

def deleteAll(request):#관리자일 경우만 전체 게시물 삭제가능하도록 하기
    deleteAll = Book.objects.all()
    deleteAll.delete()
    return redirect('homePage')