from django import forms


class UrlForm(forms.Form):

    url = forms.URLField(max_length=200, label="URL", widget=forms.TextInput(attrs={"class": "form-control"}))
