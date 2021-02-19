from django.shortcuts import render
from django.core.exceptions import ValidationError
from .forms import PostForm,PostView

from .models import posts

# Create your views here.
def postformview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts.objects.create(**data)
    else:
        form = PostForm()

    return render(request, 'postform.html', {'form': form})

def postlistview(request):
        if request.method == 'POST':
            form = PostView(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                if posts.objects.filter(user_name__user_name=data['user_name']):
                    query = posts.objects.filter(user_name__user_name=data['user_name'])
                    return render(request, 'postlist.html', {'form': form,'query':query})
                else:
                    msg = "No Post Found"
        else:
            form = PostView()
            msg=""

        return render(request, 'postlist.html', {'form': form,'msg':msg})
