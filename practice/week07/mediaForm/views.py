from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Book
from .forms import BookForm

# Create your views here.
def homePage(request):
    books=Book.objects.all()
    return render(request,"homePage.html",{'bookContents':books})

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
            return redirect('homePage') 
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
        return redirect("/mediaForm/"+str(bookId)) 

    

def delete(request,bookId):
    deleteBook=Book.objects.get(id=bookId)
    deleteBook.delete()
    return redirect('homePage')

 