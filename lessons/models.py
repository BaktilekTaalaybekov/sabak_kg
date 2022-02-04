from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name='Видео', blank=True)
    lecturer = models.CharField(max_length=150, verbose_name='Лектор')
    description = models.TextField(verbose_name='Описание')
    home_work = models.URLField(max_length=150, verbose_name='Домашнее задание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Загружен')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_lesson', kwargs={"lesson_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
