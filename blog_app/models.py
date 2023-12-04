from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_app/', verbose_name='превью',
                                null=True, blank=True)
    date_of_creation = models.DateTimeField(verbose_name='дата создания')

    view_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True,
                                       verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True,
                            blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
