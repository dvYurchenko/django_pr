#from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Posts

def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return  render(request, 'posts/posts_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'posts/posts_form.html', {'form': form})

def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/postshome.html', context)

def about(request):
    return render(request, 'about.html')


