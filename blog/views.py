from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'index.html'
    context_object_name = 'objects'
    paginate_by = 6


class UserBlogListView(ListView):
    model = Blog
    template_name = 'user_blog.html'
    context_object_name = 'objects'
    paginate_by = 6

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(UserBlogListView, self).get_context_data(**kwargs)
    #     context['current_user'] = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Blog.objects.filter(author=user)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['dp_image', 'icon_image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ['dp_image', 'icon_image', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()

        if self.request.user == blog.author:
            return True
        else:
            return False


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        blog = self.get_object()

        if self.request.user == blog.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'about.html')
