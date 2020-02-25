from django.shortcuts import render
from .models import *

# Math module
from django.db.models import Count, Q

# Pagination module.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# Home page view.
def index(request):
    # Display featured posts.
    featured = Post.objects.filter(featured=True)

    # Display latest posts.
    latest = Post.objects.order_by('-timestamp')[0:3]

    context = {
        'featured_post_list':featured,
        'latest_post_list':latest
    }
    return render(request, 'index.html', context)

# Blog listing page view.
def blog(request):
    # Display all blog posts.
    all_posts = Post.objects.all()

    # Pagination
    paginator = Paginator(all_posts, 4)
    page_num = 'page'
    page = request.GET.get(page_num)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    
    # Display recent posts.
    recent = Post.objects.order_by('-timestamp')[0:3]

    # Display category title & count.
    category_count = Post.objects.values('categories__title').annotate(Count('categories__title'))

    # Dispkay tags.
    tags = Tag.objects.all()
    
    context = {
        'posts_list':paginated_queryset,
        'page_num':page_num,
        'recent_post_list':recent,
        'category_count':category_count,
        'tags_list':tags
    }
    return render(request, 'blog.html', context)

# Blog single post detail view.
def post(request, slug):
    context = {}
    return render(request, 'post.html', context)

# Search result page view.
def search_result(request):
    queryset = Post.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        queryset = queryset.filter(
            Q(title__icontains=search_query) | Q(overview__icontains=search_query) 
        ).distinct()
        q_count = queryset.count()

    context = {
        'queryset':queryset,
        'search_query':search_query,
        'q_count':q_count
    }
    
    return render(request, 'search-result.html', context)