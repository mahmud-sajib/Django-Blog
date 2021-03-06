"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# Path modules.
from django.urls import path, re_path, include

# STATIC and MEDIA files module. 
from django.conf.urls.static import static
from django.conf import settings 

from posts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('article/<slug:slug>/', post, name='post-detail'),
    path('category/<slug:slug>/', category_detail, name='category-detail'),
    path('like/', post_like, name='post-like'),
    path('search-result/', search_result, name='search-result'),
    path('', include('authentication.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

