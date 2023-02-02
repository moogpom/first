from django import forms
from .models import Book

class BookForm(forms.ModelForm): # 장고에서 제공해주는 forms를 상수로 받아옴 
    class Meta:
        model = Book
        fields = ['title','writer','publisher','pub_date','body','image']

#        ﻿
#장고에서는 Form이라는 걸 제공해줌
#
#입력양식 form태그를 장고에서는 forms.py 객체지향적으로 만들 수 있음
#
#장점 : 데이터베이스 모델이 변해도 하나하나 바꿔주지 않아도 됨 + 유효성 검사할 수 있음
#
#﻿