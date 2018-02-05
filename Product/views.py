from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Category


@require_http_methods(['GET'])
def get_categories(request):
    response = {}
    for category in Category.CATEGORY_CHOICES:
        response[category[0]] = []
        for label in category[1]:
            response[category[0]].append(label)
    return JsonResponse(data=response)
