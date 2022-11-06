# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from .permissions import ChangePermissionRequiredMixin


class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now'] = datetime.utcnow()  Now use tag instead
        context['filterset'] = self.filterset
        context['next_publication'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    raise_exception = False
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.author = self.request.user.author
        return super().form_valid(form)


# def create_post(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/posts/')
#     return render(request, 'news/post_edit.html', {'form': form})


class PostUpdate(LoginRequiredMixin, ChangePermissionRequiredMixin, UpdateView):
    raise_exception = False
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    raise_exception = False
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_list')
