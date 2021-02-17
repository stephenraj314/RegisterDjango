from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignupForm

# Create your views here.

#def Signupview(request):
#    return HttpResponse("<h1>Hi</h1>")


def signupview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse("<h1>success</h1>")
    else:
        form = SignupForm()

    return render(request, 'form.html', {'form': form})
def success(request):
    return render(request, 'thanks.html')
