from .models import Comment, Post
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from captcha.fields import ReCaptchaField

User = get_user_model()

from captcha.widgets import ReCaptchaV2Checkbox

class PostCreateForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)



        
