from django import forms
from .models import Book

class BookForm(forms.ModelForm): # 장고에서 제공해주는 forms를 상수로 받아옴 
    class Meta:  
        model = Book
        fields = ['title','writer','publisher','pub_date','body','image']