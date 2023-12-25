from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение',
                              null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.IntegerField(verbose_name='цена за покупку')
    date_at = models.DateTimeField(verbose_name='дата создания')
    date_last_change = models.DateTimeField(verbose_name='дата последнего '
                                                         'изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='пользователь')

    is_published = models.BooleanField(default=True,
                                       verbose_name='публикация активна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            (
                "set_published_status",
                "Can publish product"
            )
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='название версии')
    is_active = models.BooleanField(default=False,
                                    verbose_name='версия активна')

    def __str__(self):
        return f"{self.name}, {self.number}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
