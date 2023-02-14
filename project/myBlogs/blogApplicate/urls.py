from django.urls import path
from .views import login_view,home_view,create_blog,all_blogs,blog_detail

urlpatterns = [
    path('',home_view,name='home'),
    path('create-blog/',create_blog,name='create_blog'),
    path('blog/',all_blogs,name='Blogs'),
     path('blog/<int:pk>/', blog_detail, name='blog_detail'),
    path('login/', login_view, name='login'),
]