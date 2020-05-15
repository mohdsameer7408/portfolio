from django.urls import path
from . import views
from .views import (
    BlogListView,
    UserBlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('user/<str:username>', UserBlogListView.as_view(), name='user-blog'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='about'),
]
