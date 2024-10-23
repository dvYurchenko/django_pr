#from lib2to3.fixes.fix_input import context
from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Posts
from django.contrib.auth.decorators import login_required


@login_required
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
    return  render(request, 'blog/about.html', context)

@login_required
def edit_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id':id}
        return render(request, 'posts/posts_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно отредактирован!')
            return redirect('home')
        else:
            messages.error(request, 'Проверь введенные данные. Ошибка!')
            return render(request, 'posts/posts_form.html', {'form':form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)
    context = {'post': post}
    if request.method == 'GET':
        return render(request, 'posts/posts_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост успешно удален!')
        return redirect('home')
