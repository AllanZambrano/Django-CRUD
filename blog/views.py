from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 

from .models import Post

class PostListView(ListView):
	model = Post
	template_name = 'post_list.html'

class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class PostCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = '__all__'

class PostUpdateView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')
