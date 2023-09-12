from django.shortcuts import render
from .utils import get_random_quote
from .models import Post


def home(request):
    posts = Post.objects.all()
    random_quote = get_random_quote()
    return render(request, 'home.html', {'random_quote': random_quote, 'posts': posts})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': posts})
