from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200, default='default_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])