from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _
# from modeltranslation.admin import TranslationAdmin


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

# class TranslateFlatPageAdmin(FlatPageAdmin, TranslationAdmin):
#     model = FlatPage
#
#
# admin.site.unregister(FlatPage, FlatPageAdmin)
# admin.site.register(FlatPage, TranslateFlatPageAdmin)
