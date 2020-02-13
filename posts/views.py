from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def post(request):
    context = {}
    return render(request, 'post.html', context)