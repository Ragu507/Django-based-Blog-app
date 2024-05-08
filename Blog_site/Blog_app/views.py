from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

##################  USER REGISTER  ########################

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

##################  USER LOGIN VIEW  ########################

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


##################  USER LOGOUT VIEW  ########################

def user_logout(request):
    logout(request)
    return redirect('index')

##################  CREATE BLOG VIEW  ########################

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        else:
            print(form.errors)
            print(form.cleaned_data)  
    else:
        form = BlogForm()
    return render(request, 'blog/create_post.html', {'form': form})

def index(request):
    blog=Blog.objects.all().order_by('time_stamp')
    return render(request,'blog/index.html',{'blog':blog})

##################  BLOG DETAIL VIEW  ########################

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})

##################  USER PROFILE VIEW  ########################

@login_required(login_url='login')
def profile(request):
    user = request.user
    blogs = Blog.objects.filter(author=user)
    return render(request, 'blog/profile.html', {'blogs': blogs,'user':user})

##################  UPDATE BLOG  ########################

@login_required(login_url='login')
def update_post(request, id):
    post = get_object_or_404(Blog, id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})

##################  DELETE BLOG  ########################

@login_required(login_url='login')
def delete_post(request, id):
    post = get_object_or_404(Blog, id=id)
    post.delete()
    return redirect('profile')