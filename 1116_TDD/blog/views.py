from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from .forms import PostForm
from .models import Post

class IndexView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['key'] = 'value'
        return context
    
index = IndexView.as_view()

class AboutView(TemplateView):
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
about = AboutView.as_view()

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
contact = ContactView.as_view()

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Post 
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()