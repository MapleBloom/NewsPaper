from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
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
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  ]

    def clean(self):
        cleaned_data = super().clean()
        for field, val in cleaned_data.items():
            if len(val) == 0:
                raise ValidationError({
                    field: 'This field should be filled'
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
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save()
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
        return user
