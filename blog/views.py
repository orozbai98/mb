from django.views.generic import ListView, DetailView # new
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'blog/post_detail.html'