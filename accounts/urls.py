from django.urls import path
from .views import ProfileUser, UserUpdate, SignUp

urlpatterns = [
    path('<int:pk>/profile/user', ProfileUser.as_view(), name='profile_user'),
    path('<int:pk>/upgrade', UserUpdate.as_view(), name='user_upgrade'),
    path('signup', SignUp.as_view(), name='mainsignup'),
]