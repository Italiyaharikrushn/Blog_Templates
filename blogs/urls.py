from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('travel/', views.travel_view, name='travel'),
    path('myself/', views.my_self_view, name='myself'),
    path('post-page/', views.post_page_view, name='post_page'),
    path('biography/', views.biography_view, name='biography'),
    path('posts/', views.post_view, name='posts'),
    path('advertisements/', views.advertisement_view, name='advertisements'),
    path('categories/', views.category_view, name='categories'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)