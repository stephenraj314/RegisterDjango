from django.shortcuts import render
from .forms import SigninForm
from signUp.models import users
from django.http import HttpResponseRedirect

def signinview(request):
    html=''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SigninForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['user_name']
            passwd=form.cleaned_data['password']
            if users.objects.filter(user_name=name,password=passwd).first():
                return HttpResponseRedirect('/thanks/')
            else:
                html="username or password not valid"
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form,'html':html})
