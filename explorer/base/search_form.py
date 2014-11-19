__author__ = 'skandeel'
from django import forms

class SearchForm(forms.Form):
    App_title = forms.CharField(max_length=256)

