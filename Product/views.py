from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Category, Product

@require_http_methods(['GET'])
def add_product(request):
    #TODO
    return render(request, 'product/add.html')

@require_http_methods(['GET'])
def delete_product(request):
    #TODO
    return render(request, 'product/delete.html')

@require_http_methods(['GET'])
def detail_product(request):
    return render(request, 'product/detail.html')

@require_http_methods(['GET'])
def edit_product(request):
    #TODO
    return render(request, 'product/edit.html')

@require_http_methods(['GET'])
def get_product(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'product/get.html', {'products': products})

@require_http_methods(['GET'])
def get_categories(request):
    response = {}
    for category in Category.CATEGORY_CHOICES:
        response[category[0]] = []
        for label in category[1]:
            response[category[0]].append(label)
    return JsonResponse(data=response)
