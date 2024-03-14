from django.shortcuts import render

# Create your views here.

def index(request):
    text = 'Hello World!'
    context = {'text': text}
    return render(request, 'index.html', context)

def contact(request):
    context = {"page":"Contact"}
    return render(request, 'contact.html',context)


def about(request):
    context = {"page": "About"}
    return render(request, 'aboutus.html', context)