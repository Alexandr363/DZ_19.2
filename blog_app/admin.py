from django.contrib import admin
from blog_app.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_of_creation')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'cost', 'category',)
#     list_filter = ('category',)
#     search_fields = ('name', 'description',)
