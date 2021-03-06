from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', { 'posts': posts })

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm()
        return render(request, 'create.html', { 'form': form })

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('index')

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = PostForm(instance = post)
        return render(request, 'update.html', { 'form': form, 'id': id })
