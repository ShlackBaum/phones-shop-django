from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting=request.GET.get('sort')
    template = 'catalog.html'
    if not sorting:
        phone_objects = Phone.objects.all()
    elif sorting=="name":
        phone_objects = Phone.objects.order_by('name')
    elif sorting=="min_price":
        phone_objects = Phone.objects.order_by('price')
    elif sorting=="max_price":
        phone_objects = Phone.objects.order_by('-price')
    context = {"phones": phone_objects,
               "sorting": sorting}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    data_on_phone_by_slag = Phone.objects.get(slug=slug)
    context = {"phone": data_on_phone_by_slag}
    return render(request, template, context)
