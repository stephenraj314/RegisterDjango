from django.shortcuts import render
from .forms import PostForm
from .models import posts

# Create your views here.
def postview(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            posts.objects.create(**data)
    else:
        form = PostForm()

    return render(request, 'postform.html', {'form': form})
