from django.urls import path
from blog_app.apps import BlogAppConfig
from blog_app.views import BlogListView, BlogCreateView, BlogDetailDetailView, \
    BlogUpdateView, BlogDeleteView

app_name = BlogAppConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='BlogCreateView'),
    path('blog/<int:pk>', BlogDetailDetailView.as_view(),
         name='BlogDetailDetailView'),
    path('blog/', BlogListView.as_view(), name='BlogListView'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='BlogUpdateView'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='BlogDeleteView'),
]
