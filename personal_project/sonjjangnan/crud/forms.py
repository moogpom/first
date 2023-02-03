from django import forms
from .models import *

# Create your models here.
class PhotoForm(forms.ModelForm):
    title = forms.CharField(label='제목', max_length=50, 
        widget=forms.Textarea(attrs={'rows':'1', 'cols': '70'}))
    body = forms.CharField(label='내용', max_length=1000, 
        widget=forms.Textarea(attrs={'rows':'15', 'cols': '70'}))
    class Meta:
        model = Photo
        fields =['title','body','image']

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields =[]