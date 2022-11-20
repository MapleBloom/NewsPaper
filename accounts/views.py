from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .forms import SignUpForm, UserForm
from .permissions import ProfileUserPermissionRequiredMixin


class ProfileUser(LoginRequiredMixin, ProfileUserPermissionRequiredMixin, DetailView):
    raise_exception = False
    permission_required = ('auth.view_user',)
    model = User
    template_name = 'accounts/profile_user.html'
    context_object_name = 'user'


class UserUpdate(LoginRequiredMixin, ProfileUserPermissionRequiredMixin, UpdateView):
    raise_exception = False
    permission_required = ('auth.change_user',)
    form_class = UserForm
    model = User
    template_name = 'accounts/user_upgrade.html'

    def get_success_url(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return f'profile/user'


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'
