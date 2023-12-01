from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, HomeListView, \
    ProductDetailDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='HomeListView'),

    path('contacts/', ContactsTemplateView.as_view(),
         name='ContactTemplateView'),

    path('product/<int:pk>', ProductDetailDetailView.as_view(),
         name='ProductDetailDetailView')
]
