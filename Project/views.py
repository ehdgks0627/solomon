from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Project

@require_http_methods(['GET'])
def create_project(request):
    #TODO
    return render(request, 'project/create.html')

@require_http_methods(['GET'])
def delete_project(request):
    #TODO
    return render(request, 'project/delete.html')

@require_http_methods(['GET'])
def detail_project(request):
    return render(request, 'project/detail.html')

@require_http_methods(['GET'])
def edit_project(request):
    #TODO
    return render(request, 'project/edit.html')

@require_http_methods(['GET'])
def get_project(request):
    return render(request, 'project/get.html')
