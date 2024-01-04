from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, HomeListView, \
    ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='HomeListView'),
    path('contacts/', ContactsTemplateView.as_view(),
         name='ContactTemplateView'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()),
         name='ProductDetailView'),
    path('create/', ProductCreateView.as_view(), name='ProductCreateView'),
    path('update/<int:pk>', ProductUpdateView.as_view(),
         name='ProductUpdateView'),
    path('delete/<int:pk>', ProductDeleteView.as_view(),
         name='ProductDeleteView'),
]
