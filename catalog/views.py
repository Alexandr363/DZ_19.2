from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from catalog.models import Product, Version
from catalog.forms import ProductForm


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    extra_context = {
        'title': 'Контакты'
    }

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f" {name}  {phone}  {message} ")
        return render(request, 'catalog/contacts.html')


class HomeListView(ListView):
    model = Product

    extra_context = {
        'title': 'Магазин'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:HomeListView')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:HomeListView')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:HomeListView')
