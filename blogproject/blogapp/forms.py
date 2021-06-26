from django import forms
# from django.forms import fields
# from django.forms.models import ModelForm
from .models import Blog

class BlogForm(forms.ModelForm):
   # ModelForm: 모델과 필드를 지정하면 모델폼이 자동으로 생성
   class Meta:
       model = Blog
       fields = ['title', 'body']
       # pub_date는 자동으로 생성되기 때문에 fields에 넣지 않음