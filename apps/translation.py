from modeltranslation.translator import register, TranslationOptions

from apps.models import Blog


@register(Blog)
class NewTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'category')

