from django import forms

class ResearchForm(forms.Form):
    Rechercher = forms.CharField(max_length=100)
