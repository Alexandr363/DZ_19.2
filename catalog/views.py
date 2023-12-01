from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from catalog.models import Product


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


class ProductDetailDetailView(DetailView):
    model = Product
