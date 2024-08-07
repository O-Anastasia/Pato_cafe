from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import DishCategory, Dish, Chefs, Gallery, Introduction, Description, Review, Reservation
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Introduction)
admin.site.register(Description)
admin.site.register(Review)
admin.site.register(Reservation)

@admin.register(DishCategory)
class DishCategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'is_visible', 'sort')
    list_editable = ('name', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)

@admin.register(Dish)
class DishAdmin(TranslationAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category')
    list_editable = ('price', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible',)
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Dish photo'


@admin.register(Chefs)
class ChefsAdmin(TranslationAdmin):
    list_display = ('photo_src_tag', 'name', 'position', 'description', 'is_visible')
    list_editable = ('is_visible', 'position',)
    list_filter = ('position', 'is_visible',)
    search_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width=50 height=50>")

    photo_src_tag.short_description = 'Chefs photo'
