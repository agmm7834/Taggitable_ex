from django import forms
from taggit.forms import TagField

from .models import Article


class ArticleForm(forms.ModelForm):
    tags = TagField(required=False, help_text="Перечислите теги через запятую.")

    class Meta:
        model = Article
        fields = ('title', 'content', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }

