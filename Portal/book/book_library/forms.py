from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='Search PYQs', max_length=100)