"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from django.urls import path

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from blog.views import PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView
from config.views import LinkListView
from comment.views import CommentView
from .custom_site import custom_site


'''
urlpatterns = [
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

# 使用 path 方法改写
urlpatterns = [
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
    path('', IndexView.as_view(), name='index'),
    path('blog/', IndexView.as_view(), name='blog-home'),
    path('blog/category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('blog/tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    path('blog/post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/search/', SearchView.as_view(), name='search'),
    path('blog/author/<int:owner_id>', AuthorView.as_view(), name='author'),
    path('blog/links/', LinkListView.as_view(), name='links'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('blog/rss|feed/', LatestPostFeed(), name='rss'),
    path('blog/sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path('blog/ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






