from django import forms
# Create the FormName class


class UrlInput(forms.Form):
    long_url = forms.URLField(label='Long Url',widget=forms.TextInput(attrs={'placeholder': "Paste your long link here"}))
    