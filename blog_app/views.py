from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, \
    DeleteView
from blog_app.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:BlogListView')


class BlogDetailDetailView(DetailView):
    model = Blog


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блог'
    }


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'date_of_creation')
    success_url = reverse_lazy('blog:BlogListView')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:BlogListView')
