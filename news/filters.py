from django_filters import FilterSet, ModelChoiceFilter, ModelMultipleChoiceFilter, DateFilter
from django.forms import DateInput
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from .models import Post, Author, Category


class PostFilter(FilterSet):
    time_in = DateFilter(
        field_name='time_in',
        lookup_expr='gt',
        label=gettext_lazy('Publication date from'),
        widget=DateInput(format='%Y-%m-%d',
                         attrs={'type': 'date'}
                         )
    )

    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        lookup_expr='exact',
        label=gettext_lazy('Author'),
        empty_label='all'
    )

    category = ModelMultipleChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label=gettext_lazy('Category'),
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
        # labels = {                              # Doesn't work this way. Field name should be defined in models.py
        #     'title': gettext_lazy('Title'),
        #     'post': gettext_lazy('post'),
        # }


class CategoryFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='',
    )
