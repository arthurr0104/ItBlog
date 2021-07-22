from captcha.fields import CaptchaField
from django import forms

from .models import Comment, Post


class UserCommentForm(forms.ModelForm):
    captcha = CaptchaField(
        error_messages={'invalid': 'Մուտքագրվածը չի համապատասխանում պատկերվածին '})

    class Meta:
        model = Comment
        exclude = ('is_published', 'author')

        fields = ('post', 'text', 'is_published', 'author')

        widgets = {'post': forms.HiddenInput(),

                   'text': forms.Textarea(attrs={'class': 'block clear', 'id': 'exampleFormControlTextarea1',
                                                 'rows': '3'})
                   }
