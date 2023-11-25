from django.shortcuts import render

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


def goods(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары'
    }
    return render(request, 'main/goods.html', context)
