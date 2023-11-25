from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

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

    @property
    def description_100(self):
        return self.description[:100]

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
