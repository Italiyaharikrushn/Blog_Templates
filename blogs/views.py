# from django.shortcuts import render, redirect
# from .models import Blog, Travel, MySelf, PostPage
# from django.http import HttpResponse


# First section
# Blog entry creation
# def create_entry(request):
#     if request.method == "POST":
#         blog_category = request.POST.get("category")
#         title = request.POST.get("title")
#         blog_image_url = request.POST.get("image_url")
#         blog_post_title = request.POST.get("post_title")

#         if blog_category and title and blog_post_title:
#             blog_entry = Blog(
#                 category=blog_category,
#                 title=title,
#                 image_url=blog_image_url,
#                 post_title=blog_post_title,
#             )
#             blog_entry.save()
#             return redirect("entry_created")

#         else:
#             context = {"error_message": "Please fill in all required fields."}
#             return render(request, "blogs/create_entry.html", context)

#     return render(request, "blogs/create_entry.html")


# # Success Message
# def entry_created(request):
#     return render(
#         request,
#         "blogs/entry_created.html",
#         {"message": "Blog entry created successfully!"},
#     )


# # Display all blog
# def blog_view(request):
#     blog_entries = Blog.objects.all()
#     return render(request, "blogs/blog.html", {"blog_entries": blog_entries})


# # Second Section: Travel Functionality
# # Add a travel entry
# def add_travel_entry(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         image_url = request.POST.get("image_url")
#         read_more_link = request.POST.get("read_more_link")

#         if title and description:
#             travel_entry = Travel(
#                 title=title,
#                 description=description,
#                 image_url=image_url,
#                 read_more_link=read_more_link,
#             )
#             travel_entry.save()
#             return redirect("travel_list")

#         else:
#             context = {"error_message": "Please fill in all required fields."}
#             return render(request, "travel/add_travel_entry.html", context)

#     return render(request, "travel/add_travel_entry.html")


# # Third Section: Self Introduction
# def create_myself(request):
#     if request.method == "POST":
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         read_more_link = request.POST.get("read_more_link")
#         video = request.FILES.get("video")

#         if not title or not description:
#             return HttpResponse("Title and Description are required.", status=400)

#         myself_instance = MySelf(
#             title=title,
#             description=description,
#             read_more_link=read_more_link,
#             video=video,
#         )
#         myself_instance.save()

#         return HttpResponse("MySelf instance created successfully.")

#     return render(request, "myself/create_myself.html")


# # four Section: post_list
# def post_list(request):
#     posts = PostPage.objects.all()
#     return render(request, "post_list.html", {"posts": posts})


# def post_create(request):
#     if request.method == "POST":
#         form = PostPage(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")
#     else:
#         form = PostPage()

#     return render(request, "post_create.html", {"form": form})

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
    return render(request, "blogs/blog.html", {"blogs": blogs})


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
