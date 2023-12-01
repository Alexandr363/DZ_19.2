from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_app/', verbose_name='превью',
                                null=True, blank=True)
    date_of_creation = models.DateTimeField(verbose_name='дата создания')
    view_count = models.IntegerField(default=0, verbose_name='просмотры')
