from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from product.models import Product
from project.models import Project
from .models import Order


@login_required(login_url='/')
@require_http_methods(['POST'])
def create_order(request):
    '''
            order = Order.objects.create_order(owner=owner, product=product, project=project, title=title, state=state,
                                               payment_method=payment_method,
                                               price=price, period=period, tags=tags)
    '''
    product = Product.objects.get(id=request.POST.get('product_id'))
    project = Project.objects.get(id=request.POST.get('project_id'))
    order = Order.objects.create_order(owner=request.user,
                                       product=product,
                                       project=project,
                                       payment_method=-1)
    # TODO payment_method not implemented

    return redirect('/product/detail/{}/'.format(product.id))
