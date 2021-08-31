from django import forms


class PostSearch(forms.Form):
    body = forms.CharField(label='Введите строку для поиска', required=False)