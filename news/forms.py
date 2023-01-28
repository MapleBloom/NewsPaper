from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post',
                  'title',
                  'text',
                  'category',
                  # 'author',
                  ]
        labels = {
            'category': gettext_lazy('Category'),
        }

    def clean(self):
        cleaned_data = super().clean()
        title, text = cleaned_data.get('title'), cleaned_data.get('text')
        if text != 'In progress' and len(text) < 20:
            raise ValidationError({
                'text': _('Meaningless publication under 20 symbols demands upgrade.')
            })
        if title is not None and title.lower() in text.lower():
            err_text = _("Rewrite title, don't repeat yourself.")
            raise ValidationError({'title': err_text})
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(
                _("It's title, start with Capital!")
            )
        return title
