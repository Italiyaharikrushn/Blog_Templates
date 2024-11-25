# get all data on database
from django.shortcuts import render
from .models import (
    Blog,
    Travel,
    MySelf,
    PostPage,
    Biography,
    Post,
    Advertisement,
    Category,
)

def blog_view(request):
    blogs = Blog.objects.all()
    travels = Travel.objects.all()
    myself = MySelf.objects.all()
    post_pages = PostPage.objects.all()
    biographies = Biography.objects.all()
    posts = Post.objects.all()
    advertisements = Advertisement.objects.all()
    categories = Category.objects.all()
    return render(request, "blogs/blog.html", {"blogs": blogs, "travels": travels, "myself": myself,"post_pages": post_pages, "biographies": biographies, "posts": posts, "advertisements": advertisements, "categories": categories})


def travel_view(request):
    travels = Travel.objects.all()
    return render(request, "blogs/travel_template.html", {"travels": travels})


def my_self_view(request):
    myself = MySelf.objects.all()
    return render(request, "blogs/myself_template.html", {"myself": myself})


def post_page_view(request):
    post_pages = PostPage.objects.all()
    return render(request, "blogs/post_page_template.html", {"post_pages": post_pages})


def biography_view(request):
    biographies = Biography.objects.all()
    return render(request, "blogs/biography_template.html", {"biographies": biographies})


def post_view(request):
    posts = Post.objects.all()
    return render(request, "blogs/post_template.html", {"posts": posts})


def advertisement_view(request):
    advertisements = Advertisement.objects.all()
    return render(
        request, "blogs/advertisement_template.html", {"advertisements": advertisements}
    )


def category_view(request):
    categories = Category.objects.all()
    return render(request, "blogs/category_template.html", {"categories": categories})