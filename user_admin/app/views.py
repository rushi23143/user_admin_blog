from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def modules(request):
    if request.method == "POST":
        button = request.POST['button']
        if button == 'admin':
            return redirect('admin_page')
        elif button == 'user':
            return redirect('login')
    return render(request, 'modules.html')

def login(request):
    if request.user.is_authenticated:
        auth.logout(request)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong username and password.')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken!')
                return redirect('signup')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.info(request, "Successfully registered!\n login now. ")
                user.save()
                return redirect('login')
        except Exception as e:
            print(e)
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    blog = Blog.objects.all()
    return render(request, 'index.html', {'blog':blog})

def blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        title = request.POST['title']
        desc = request.POST['description']
        Blog.objects.create(title=title, desc=desc)
        return redirect('index')
    return render(request, "blog.html")

def edit_blog(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    store = Blog.objects.get(id=id)
    if request.POST:
        title = request.POST['title']
        desc = request.POST['description']

        store.title = title
        store.desc = desc
        store.save()
        return redirect("index")
    return render(request, 'edit_blog.html', {'store':store})

def delete_blog(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    Blog.objects.get(pk=id).delete()
    return redirect('user_blog')

def del_blog(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    Blog.objects.get(pk=id).delete()
    return redirect('index')

def admin_page(request):
    us = Blog.objects.all()
    a = User.objects.all()
    return render(request, "admin_page.html", {'us':us, 'a':a})

def users(request):
    a = User.objects.all().exclude(is_staff=True)
    return render(request, 'users.html', {'a':a})

def user_blog(request):
    bl = Blog.objects.all()
    return render(request, 'user_blog.html', {'bl':bl})