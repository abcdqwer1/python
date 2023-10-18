from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm

def postlist(request):
    posts = Post.objects.all()
    return render(request, 'blog/postlist.html', {'posts':posts})

def postdetail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/postdetail.html', {'post':post})

def posttag(request, tag):
    posts = Post.objects.filter(tags__name__iexact=tag)
    return render(request, 'blog/postlist.html', {'posts':posts})