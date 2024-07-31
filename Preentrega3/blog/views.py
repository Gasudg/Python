from django.shortcuts import render, redirect
from .forms import AuthorForm, CategoryForm, PostForm
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'blog/create_author.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'blog/create_category.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'blog/search_posts.html', {'results': results, 'query': query})

