from django.urls import path

from .views import (
PostListView,
PostUpdateView,
PostDetailView,
PostCreateView,
PostDeleteView,
)

urlpatterns = [
path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
	path('post/new/', PostCreateView.as_view(), name='post_new'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
	path('post/<int:pk>/edit/',	PostUpdateView.as_view(), name='post_edit'),
	path('', PostListView.as_view(), name='home'),
]