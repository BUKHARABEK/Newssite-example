from django import forms

from .models import *


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Choose category",
                                      label="Category: ")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Choose author", required=False,
                                    label="Author: ")

    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'is_published', 'photo', 'author', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class UploadFileForm(forms.Form):
    file = forms.FileField(label='File')
