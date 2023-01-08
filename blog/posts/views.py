from django.shortcuts import render
from .models import Posts

# Create your views here.
def home(request):
    posts = Posts.objects.all()
    return render(request, 'home.html', {'posts': posts})

def posts(request):
    posts = Posts.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post(request, pk):
    posts = Posts.objects.get(id=pk)
    return render(request, 'post.html', {'post': posts})
