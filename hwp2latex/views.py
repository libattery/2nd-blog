from django.shortcuts import render
from django.http import HttpResponseRedirect

import hml_equation_parser as hp

from .forms import eqInputForm

def converter(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = eqInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            hwpeq = form.cleaned_data['input_eq'] #           hwpeq = your_name
            # process the data in form.cleaned_data as required
            latexeq = hp.eq2latex(hwpeq)
            # redirect to a new URL:
#            return HttpResponseRedirect('')
#            return HttpResponseRedirect('')
            form = eqInputForm()
            return render(request, 'hwp2latex/converter.html', {'hwpeq': hwpeq,'latexeq': latexeq,'form': form})
#            return redirect('converter',{'form': form})


    # if a GET (or any other method) we'll create a blank form
    else:
        form = eqInputForm()

    return render(request, 'hwp2latex/converter.html', {'form': form})
