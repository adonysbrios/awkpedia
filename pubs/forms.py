from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Article, Publication

class ArticleForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)

class PublicationForm(forms.Form):
    content = MarkdownxFormField()