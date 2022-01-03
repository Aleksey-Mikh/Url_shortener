from django import forms


class UrlForm(forms.Form):

    url = forms.CharField(max_length=200, label="URL", widget=forms.TextInput(attrs={"class": "form-control"}))
