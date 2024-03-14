from django.shortcuts import render

from product.models import Product


# Create your views here.

def index(request):
    trendy_product = Product.objects.order_by('?')[:8]
    context = {'trendy_product': trendy_product}
    return render(request, 'index.html', context)

def contact(request):
    context = {"page":"Contact"}
    return render(request, 'contact.html',context)


def about(request):
    context = {"page": "About"}
    return render(request, 'aboutus.html', context)