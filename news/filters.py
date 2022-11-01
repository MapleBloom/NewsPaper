from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateFilter
from django.forms import DateInput
from .models import Post, Author, Category


class PostFilter(FilterSet):
    time_in = DateFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Publication date from',
        widget=DateInput(format='%Y-%m-%d',
                         attrs={'type': 'date'}
                         )
    )

    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        lookup_expr='exact',
        label='Author',
        empty_label='all'
    )

    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=False,
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            #'author__userAuthor': ['exact'],
            'post': ['exact'],
            #'category': ['exact'],
            #'time_in.date': ['gt'],
        }
