from django.urls import path
from .views import PostsList, PostDetail, PostCreate


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create', PostCreate.as_view(), name='post_edit'),
    # path('<int:pk>/edit', PostDetail.as_view()),
    # path('<int:pk>/delete', PostDetail.as_view()),
]
