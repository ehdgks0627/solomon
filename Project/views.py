from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Project


@login_required(login_url='/')
@require_http_methods(['GET', 'POST'])
def create_project(request):
    if request.method == 'GET':
        return render(request, 'project/create.html')
    elif request.method == 'POST':
        project = Project(owner=request.user,
                          title=request.POST.get("title"),
                          description=request.POST.get("description"),
                          price=request.POST.get("price"),
                          period=request.POST.get("period"),
                          category=request.POST.get("category"),
                          file=request.FILES.get("file"))
        project.save()
        return redirect('/project/get/{}/'.format(project.id))
    else:
        return None  # ERROR


@require_http_methods(['GET'])
def delete_project(request):
    # TODO
    return render(request, 'project/delete.html')


@require_http_methods(['GET'])
def detail_project(request):
    return render(request, 'project/detail.html')


@require_http_methods(['GET'])
def edit_project(request):
    # TODO
    return render(request, 'project/edit.html')


@require_http_methods(['GET'])
def get_project(request):
    return render(request, 'project/get.html')
