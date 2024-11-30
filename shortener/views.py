from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import ShortenedURL

# Home Page
def home(request):
    return render(request, 'shortener/index.html')

# User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'shortener/register.html')

# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials!")
    return render(request, 'shortener/login.html')

# User Logout
def user_logout(request):
    logout(request)
    return redirect('home')

# Dashboard
@login_required
def dashboard(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        new_url = ShortenedURL.objects.create(
            original_url=original_url, 
            user=request.user
        )
        new_url.save()
        return redirect('dashboard')
    user_urls = ShortenedURL.objects.filter(user=request.user)
    return render(request, 'shortener/dashboard.html', {'urls': user_urls})

# Redirect to Original URL
def redirect_to_url(request, short_url):
    url = get_object_or_404(ShortenedURL, short_url=short_url)
    url.clicks += 1
    url.save()
    return redirect(url.original_url)

