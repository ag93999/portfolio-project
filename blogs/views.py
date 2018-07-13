from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblog(request):
    """
    This view will show all the blog posts.
    """
    blogs = Blog.objects.all
    return render(request, 'blogs/allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    """
    This view will show the details of a specific blog.
    """
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog': detailblog})