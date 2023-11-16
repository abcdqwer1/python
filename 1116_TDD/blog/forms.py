from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] 
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control postform'}),
            'content': forms.Textarea(attrs={'class': 'form-control postform', 'rows': 8, 'placeholder' : "글을 작성해주세요"}),
        }