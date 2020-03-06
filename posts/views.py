from django.shortcuts import render, redirect, get_object_or_404

# Http modules.
from django.http import HttpResponse, HttpResponseRedirect

# Import models
from .models import *

# Model Forms.
from .forms import CommentForm

# Math module.
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
    # Display specific post by slug.
    post = get_object_or_404(Post, slug=slug)

    # Display all comments of a specific post.
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    # Comment form.
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            reply_id = request.POST.get('comment_id')
            if reply_id:
                qs = Comment.objects.get(id=reply_id)
            else:
                None

            # passing User Id, Post Id & Reply of a Comments' Id to DB 
            form.instance.user = request.user
            form.instance.post = post
            form.instance.reply = qs
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()
    
    # Display recent posts (widget area).
    recent = Post.objects.order_by('-timestamp')[0:3]

    # Display category title & count (widget area).
    category_count = Post.objects.values('categories__title').annotate(Count('categories__title'))

    # Display tags (widget area).
    tags = Tag.objects.all()

    

    context = {
        'post':post,
        'comments':comments,
        'recent_post_list':recent,
        'category_count':category_count,
        'tags_list':tags,
        'form':form,
    }
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