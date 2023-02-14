from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from .models import Blog
from .forms import BlogForm


def home_view(request):
    return render(request,'blogApp/home.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            return redirect('home')
        else:
            # show error message
            return render(request, 'blogApp/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'blogApp/login.html')



def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'blogApp/create_blog.html', {'form': form})



def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogApp/all_blogs.html', {'blogs': blogs})



def blog_detail(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogApp/blog_detail.html', {'blog': blog})