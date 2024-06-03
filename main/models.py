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





