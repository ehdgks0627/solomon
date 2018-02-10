from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Category, Product
from contract.models import Contract
from order.models import Order


@login_required(login_url='/')
@require_http_methods(['GET', 'POST'])
def create_product(request):
    if request.method == 'GET':
        return render(request, 'product/create.html')
    elif request.method == 'POST':
        # TODO img field
        product = Product(owner=request.user,
                          title=request.POST.get("title"),
                          category=request.POST.get("category"),
                          img=request.FILES.get("img"),
                          content=request.POST.get("content"),
                          one_line_introduce=request.POST.get("one_line_introduce"),
                          as_rule=request.POST.get("as_rule"),
                          refund_rule=request.POST.get("refund_rule"))
        product.save()
        return redirect('/product/get/{}/'.format(product.id))
    else:
        return None  # ERROR


@login_required(login_url='/')
@require_http_methods(['GET'])
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if product and product.owner == request.user or request.user.is_staff:
        product.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@require_http_methods(['GET'])
def detail_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product/detail.html', {'product': product})


@login_required(login_url='/')
@require_http_methods(['GET'])
def edit_product(request):
    # TODO is request.user has permission?
    order_id = request.GET.get("order_id")
    order = Order.objects.get(id=order_id)
    contract = Contract.objects.get(order=order)
    if request.method == 'GET':
        return render('product/edit.html', {'contract': contract})
    elif request.method == 'POST':
        # TODO
        raise NotImplementedError
        return HttpResponse("")
    else:
        return None  # ERROR


@require_http_methods(['GET'])
def get_product(request, category=None):
    if category:
        products = Product.objects.get(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'product/get.html', {'products': products})


@require_http_methods(['GET'])
def get_categories(request, language):
    response = {}
    for category in Category.CATEGORY_CHOICES:
        response[category[0][language]] = []
        for label in category[1]:
            response[category[0][language]].append([label[0], label[1][language]])
    return JsonResponse(data=response)
