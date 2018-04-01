from django import forms
from blog.models import Url


class UrlForm(forms.ModelForm):
    url = forms.URLField(help_text="Please enter the blog url")
    # upa = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # pda = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # created_on = forms.DateTimeField(widget=forms.HiddenInput())

    class Meta:
        model = Url
        fields = ('url',)