from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.forms import ContactForm
from home.models import ContactFormMessage
from product.models import Product


# Create your views here.

def index(request):
    trendy_product = Product.objects.order_by('?')[:8]
    context = {'trendy_product': trendy_product}
    return render(request, 'index.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # print(form.cleaned_data['name'])
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/contact')


    form = ContactForm
    context = {"page":"İletişim","form":ContactForm}
    return render(request, 'contact.html',context)


def about(request):
    context = {"page": "About"}
    return render(request, 'aboutus.html', context)

def mostReviews(request):
    urunler = Product.objects.filter(category_id=id)

    context = {
               "urunler": urunler}
    return render(request, 'content.html', context)