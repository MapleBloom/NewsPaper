from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        commons = Group.objects.get(name="commons")
        user.groups.add(commons)
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
