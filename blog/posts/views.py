from django.shortcuts import render
from .utils import get_random_quote
from .models import Post


def home(request):
    posts = Post.objects.all()
    random_quote = get_random_quote()
    return render(request, 'home.html', {'random_quote': random_quote, 'posts': posts})


def posts(request):
    query = request.GET.get('q')
    sort_option = request.GET.get('sort')
    posts = Post.objects.all()

    if query:
        posts = posts.filter(title__icontains=query)

    if sort_option == '':
        posts = posts.order_by('created_at')
    elif sort_option == 'title':
        posts = posts.order_by('title')

    return render(request, 'posts.html', {'query': query, 'sort_option': sort_option, 'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': posts})
