from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def product(request):
    return render(request, 'product.html', {})

def category(request):
    return render(request, 'category.html', {})

def allproducts(request):
    return render(request, 'allproducts.html', {})