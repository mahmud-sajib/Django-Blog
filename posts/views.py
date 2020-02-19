from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    # Display featured post.
    featured = Post.objects.filter(featured=True)

    # Display latest post.
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'featured_post_list':featured,
        'latest_post_list':latest
    }
    return render(request, 'index.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def post(request):
    context = {}
    return render(request, 'post.html', context)