from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
# from django.shortcuts import render
# from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Category
from .filters import PostFilter, CategoryFilter
from .forms import PostForm
from .permissions import ChangePermissionRequiredMixin, CreatePermissionRequiredMixin
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .tasks import new_post_message, send_something
from django.core.cache import cache
# import logging

# logger = logging.getLogger(__name__)


class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news/posts.html'
    context_object_name = 'posts'
    paginate_by = 4

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

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        print('get from cashe: ', obj)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            print('set to cashe: ', obj)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj


class PostsByCategory(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news/posts_by_cat.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CategoryFilter(self.request.GET, queryset)
        self.cat = None
        for k, v in self.request.GET.items():
            if k == 'category':
                self.cat = Category.objects.get(id=v)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['cat'] = self.cat
        if self.cat:
            context['is_subscriber'] = self.request.user in self.cat.userCategory.all()
        else:
            context['is_subscriber'] = None
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.userCategory.add(user)
    next = request.GET.get('next')
    # send_mail(
    #     subject=f"You have subscribed at '{category}' publications of our great News Portal",
    #     message=f"Dear, {user}!\n\n From now you are up to date in '{category}' publications.",
    #     from_email=DEFAULT_FROM_EMAIL,
    #     recipient_list=[user.email]
    # )
    html_content = render_to_string(
        'news/subscribed.html',
        {
            'category': category,
            'user': user,
        }
    )
    msg = EmailMultiAlternatives(
        subject=f"You have subscribed at '{category}' publications of our great News Portal",
        body='',    # may be request.POST['..'] , but we use template
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponseRedirect(next)


@login_required
def unsubscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.userCategory.remove(user)
    next = request.GET.get('next')
    send_mail(
        subject=f"You have unsubscribed from '{category}' publications of our great News Portal",
        message=f"Dear, {user}!\n\n From now you do not follow '{category}' publications.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email]
    )
    return HttpResponseRedirect(next)


class PostCreate(LoginRequiredMixin, CreatePermissionRequiredMixin, CreateView):
    raise_exception = False
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'news/post_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_permission'] = self.has_permission
        return context

    def form_valid(self, form):
        newpost = form.save(commit=False)
        newpost.author = self.request.user.author
        response = super().form_valid(form)
        pk = form.instance.pk
        # new_post_message.delay(pk)                 uncomment to send e-mails about new post
        return response


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


class TryCeleryView(View):
    def get(self, request):
        send_something.delay()
        return HttpResponse('Hello from celery!')
