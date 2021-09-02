from django import forms

import core.models


class PostSearch(forms.Form):
    body = forms.CharField(label='Введите строку для поиска', required=False)


class PostEdit(forms.ModelForm):
    class Meta:
        model = core.models.Post
        fields = ('title', 'body', 'author')
        widgets = {'author': forms.HiddenInput()}
