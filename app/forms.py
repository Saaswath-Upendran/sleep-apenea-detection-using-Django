from django import forms
from .models import *




class PredictionForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField()
    cp = forms.IntegerField()
    tresbps = forms.IntegerField()
    chol = forms.IntegerField()
    fbs = forms.IntegerField()
    restecg = forms.IntegerField()
    thalach = forms.IntegerField()
    exang = forms.IntegerField()
    oldpeak = forms.IntegerField()
    slope = forms.IntegerField()
    ca = forms.IntegerField()
    thal = forms.IntegerField()




