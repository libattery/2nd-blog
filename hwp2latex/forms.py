from django import forms

class eqInputForm(forms.Form):
    input_eq = forms.CharField(label='HWP equation ', max_length=300)
