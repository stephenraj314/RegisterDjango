from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignupForm
from .models import users
import bcrypt

# Create your views here.

#def Signupview(request):
#    return HttpResponse("<h1>Hi</h1>")


def signupview(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            data.pop('Repassword')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(data['password'].encode("utf-8"), salt)
            data['password']= hashed.decode("utf-8")
            users.objects.create(**data)
            print(data)
        #return HttpResponse("<h1>success</h1>")
    else:
        form = SignupForm()

    return render(request, 'form.html', {'form': form})

def success(request):
    return render(request, 'thanks.html')
