from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import SearchForm
from product.forms import CommentForm
from product.models import Category, Product, Images, Comment


def categoryProducts(request, id, slug):
    urunKategori = Category.objects.get(id=id)
    urunler = Product.objects.filter(category_id=id)

    context = {"urunKategori": urunKategori,
               "urunler": urunler}
    return render(request, 'shop.html', context)

def shop(request):
    urunler = Product.objects.all()
    urunlist = Product.objects.values('category__slug').distinct()
    #urunlist = Category.objects.values('slug')
    context = {"urunler": urunler, "urunlist": urunlist}
    return render(request, 'shop.html', context)

def productDetail(request, id, slug):
    urun = Product.objects.get(id=id)
    urun.reviewsCount = urun.reviewsCount + 1
    urun.save()
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id)
    context = {"urun": urun, "images": images, "comments": comments}
    return render(request, 'product-details.html', context)

def mostViewedProducts(request):
    urun = Product.objects.all()
    mostviews = urun.values('reviewsCount').distinct()
    return mostviews

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        print(form)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
            context = {"urunler": results}
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/shop/search')


def addComment(request, id):

    url = request.META.get('HTTP_REFERER')  # geldiğimiz sayfanın url bilgisini verir
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            print('addcomment')
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            current_user = request.user
            data.user_id = current_user.id
            data.product_id = id
            data.save()
            messages.success(request, "yorumunuz başarıyla kaydedildi")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)


