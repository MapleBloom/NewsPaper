from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post',
                  'title',
                  'text',
                  'category',
                  'author',
                  ]

    def clean(self):
        cleaned_data = super().clean()
        title, text = cleaned_data.get('title'), cleaned_data.get('text')
        if text != 'In progress' and len(text) < 20:
            raise ValidationError({
                'text': 'Meaningless publication under 20 symbols demands upgrade.'
            })
        if title is not None and title.lower() in text.lower():
            raise ValidationError({'title': "Rewrite title, don't repeat yourself."})
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0].islower():
            raise ValidationError(
                "It's title, start with Capital!"
            )
        return title
