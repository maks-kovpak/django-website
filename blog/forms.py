from django import forms

from .models import ArticleImage


class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=False)

    class Meta:
        model = ArticleImage
        fields = "__all__"
