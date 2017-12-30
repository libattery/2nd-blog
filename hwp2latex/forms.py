from django import forms

#class eqInputForm(forms.Form):
#    input_eq = forms.CharField(label='HWP equation ', max_length=500)

from .models import ConversionLog

class eqInputForm(forms.ModelForm):

    class Meta:
        model = ConversionLog
        fields = ('hwp_eq',)
