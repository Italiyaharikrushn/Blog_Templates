from django.db import models

class Blog(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='profile_images/')
    post_title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Travel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to='profile_images/')
    # date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_more_link = models.URLField(blank=True, null=True)


class MySelf(models.Model):
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    read_more_link = models.URLField(blank=True, null=True)

class PostPage(models.Model):
    image_url = models.ImageField(upload_to='profile_images/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    read_more_link = models.URLField(blank=True, null=True)

class Biography(models.Model):
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    google_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

class Post(models.Model):
    header = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    status = models.CharField(max_length=50, blank=True, null=True)
    
class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisements/')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    item_count = models.PositiveIntegerField(default=0)
    