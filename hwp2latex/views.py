from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import ConversionLog

import hml_equation_parser as hp

from .forms import eqInputForm

def converter(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = eqInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
#            hwpeq = form.cleaned_data['input_eq'] #           hwpeq = your_name
            # process the data in form.cleaned_data as required
            conversionlog = form.save(commit=False)
            conversionlog.created_date = timezone.now()
#            latexeq = hp.eq2latex(hwpeq)
            conversionlog.latex_eq = hp.eq2latex(conversionlog.hwp_eq)
            conversionlog.save()
            form = eqInputForm()
#            return render(request, 'hwp2latex/converter.html', {'hwpeq': hwpeq,'latexeq': latexeq,'form': form})
            return render(request, 'hwp2latex/converter.html', {'hwpeq': conversionlog.hwp_eq,'latexeq': conversionlog.latex_eq,'form': form})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = eqInputForm()
    return render(request, 'hwp2latex/converter.html', {'form': form})

@login_required
def conversionlog(request):
    conversionlogs = ConversionLog.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'hwp2latex/conversionlog.html', {'conversionlogs': conversionlogs})
