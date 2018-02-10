from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from contract.models import Contract
from order.models import Order


@require_http_methods(['GET'])
def detail_contract(request, contract_id):
    return render(request, 'contract/detail.html')


@login_required(login_url='/')
@require_http_methods(['GET'])
def edit_contract(request, contract_id):
    # TODO is request.user has permission?
    contract = Contract.objects.filter(id=contract_id)
    if request.method == 'GET':
        return render(request, 'contract/edit.html', {'contract': contract})
    elif request.method == 'POST':
        # TODO
        raise NotImplementedError
        return HttpResponse("")
    else:
        return None  # ERROR


@require_http_methods(['GET'])
def form_contract(request, contract_id):
    # TODO is request.user has permission?
    contract = Contract.objects.filter(id=contract_id)
    return render(request, 'contract/form.html', {'contract': contract})
