from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.utils.translation import gettext as _

from news.models import Author


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
        return user


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin)
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [_('first_name'),
                  _('last_name'),
                  _('username'),
                  _('email'),
                  ]

    def clean(self):
        cleaned_data = super().clean()
        for field, val in cleaned_data.items():
            if len(val) == 0:
                raise ValidationError({
                    field: _('This field should be filled')
                })
        return cleaned_data

    def save(self, commit=True):
        user = super().save()
        if not hasattr(user, 'author'):
            Author.objects.create(userAuthor_id=user.pk)
            authors = Group.objects.get(name="authors")
            user.groups.add(authors)
        return user


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label=_('Email'))
    first_name = forms.CharField(label=_('First name'))
    last_name = forms.CharField(label=_('Last name'))

    class Meta:
        model = User
        fields = [_('username'),
                  _('first_name'),
                  _('last_name'),
                  _('email'),
                  _('password1'),
                  _('password2'),
                  ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save()
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
        return user
