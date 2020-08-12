from django import forms

class NumberInputForm(forms.Form):
    a=forms.IntegerField(required=True,label="Enter First Number ", widget=forms.NumberInput(attrs={'class':'form-control'}))
    b=forms.IntegerField(required=True,label="Enter Second Number ",widget=forms.NumberInput(attrs={'class':'form-control'}))
