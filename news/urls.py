from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (PostsList, PostDetail, PostsByCategory,
                    NewsList, ArticlesList,
                    PostCreate, PostUpdate, PostDelete,
                    subscribe, unsubscribe, set_timezone,
                    TryCeleryView)


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('news', NewsList.as_view(), name='news_list'),
    path('articles', ArticlesList.as_view(), name='articles_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts-by-category', PostsByCategory.as_view(), name='posts_by_cat'),
    path('posts-by-category/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('posts-by-category/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
    path('create', PostCreate.as_view(), name='post_edit'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),
    path('test-celery', cache_page(60*1)(TryCeleryView.as_view()), name='test_celery'),
    path('set_timezone', set_timezone, name='set_timezone'),
]
