from django import forms
# Create the FormName class


class UrlInput(forms.Form):
    long_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': "Paste your long link here"}))
    