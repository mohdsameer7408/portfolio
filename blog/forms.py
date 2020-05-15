from django import forms
from .models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['dp_image', 'icon_image', 'description']
