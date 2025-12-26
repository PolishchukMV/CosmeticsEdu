from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image_url = models.URLField(blank=True, verbose_name='Ссылка на изображение (опционально)')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Текст новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image_url = models.URLField(blank=True, verbose_name='Ссылка на изображение новости (опционально)')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']