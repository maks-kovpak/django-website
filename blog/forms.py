from django import forms

from .models import ArticleImage


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(widget=MultipleFileInput(), required=False)

    class Meta:
        model = ArticleImage
        fields = "__all__"
