from django.db import models
from ckeditor.fields import RichTextField


class Introduction(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="introduction/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Приветствие"
        verbose_name_plural = "Приветствия"
        ordering = ['name']


class Description(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="description/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'
        ordering = ['name']


class Review(models.Model):
    name = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="review/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['name']


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['name']


class Chefs(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='chefs/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Повар'
        verbose_name_plural = 'Повара'
        ordering = ['name']


class DishCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='dishcategories/', blank=True, null=True)

    def __iter__(self):
        for item in self.dishes.filter(is_visible=True):
            yield item

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория блюд'
        verbose_name_plural = 'Категория блюд'
        ordering = ['-sort']

class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
    sort = models.PositiveIntegerField()

    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['sort']

class Reservation(models.Model):
    # phone_regex = RegexValidator(regex=r'^\+?(380)?\d{9,15}$',
    #                              message="Phone number must be entered in the format: '+999999999'. "
    #                                      "Up to 15 digits allowed.")

    name = models.CharField(max_length=255)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    people = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['-date_created']





