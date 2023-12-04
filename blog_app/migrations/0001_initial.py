# Generated by Django 4.2.7 on 2023-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_app/', verbose_name='превью')),
                ('date_of_creation', models.DateTimeField(verbose_name='дата создания')),
                ('view_count', models.IntegerField(default=0, verbose_name='просмотры')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]