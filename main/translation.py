from modeltranslation.translator import TranslationOptions, register
from .models import Description, Review, Chefs, Dish, DishCategory

@register(Description)
class DescriptionTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Chefs)
class ChefsTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description')

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('name', 'review')

@register(Dish)
class DishTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(DishCategory)
class DishCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


