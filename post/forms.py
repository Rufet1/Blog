from django import forms
from .models import Post, Comment,Category,HomeImage
from captcha.fields import ReCaptchaField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'category',
        ]

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = [
            'content'
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'home_show'
        ]

class HomeForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = [
            'image',
            'content',
            
        ]