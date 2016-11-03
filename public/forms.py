from django import forms
from .models import Post, Comment

from django_markdown.fields import MarkdownFormField
from django_markdown.widgets import MarkdownWidget

class PostForm(forms.ModelForm):
  text = forms.CharField(widget=MarkdownWidget())
  class Meta:
    model = Post
    fields = ('title', 'text')

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'text')
    exclude = ['post']