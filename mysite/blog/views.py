from django.shortcuts import render, redirect

from . models import Post

def home(request):
    return redirect('post_list')

def post_list(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('post_list')
    return render (request, 'blog/post_detail.html', {'post': post})
