from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.models import Blog


@admin.register(Blog)
class NewAdmin(TranslationAdmin):
    pass
