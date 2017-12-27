from django import forms

class eqInputForm(forms.Form):
    input_eq = forms.CharField(label='HWP equation', max_length=300)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
