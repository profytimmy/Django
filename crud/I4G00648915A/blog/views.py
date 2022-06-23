from django.views.generic.edit import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy("blog:all")


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy("blog:all")



class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy("blog:all")