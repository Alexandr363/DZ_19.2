from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        massage = request.POST.get('massage')
        print(f" {name}  {phone}  {massage}")
    return render(request, 'main/contacts.html', context)


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Магазин'
    }
    return render(request, 'main/home.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'object_list': product
    }
    return render(request, 'main/product.html', context)
