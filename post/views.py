from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def add(request):
    if request.method == "POST":
        title = request.POST['title']
        detail = request.POST['detail']
        Post.objects.create(title=title, detail=detail)
        messages.success(request, 'Data has been added!')
    return render(request, 'add.html')

def update(request, id):
    if request.method == 'POST':
        title = request.POST['title']
        detail = request.POST['detail']
        Post.objects.filter(id=id).update(title=title, detail=detail)
        messages.success(request, 'Data has been updated!')
    post = Post.objects.get(id=id)
    return render(request, 'update.html', {'post':post})

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return redirect('/')

def search(request):
    q = request.GET['q']
    posts = Post.objects.filter(title__icontains=q).order_by('-id')
    return render(request, 'search.html', {'posts':posts})