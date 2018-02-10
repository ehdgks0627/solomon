from django.shortcuts import render
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)


# TODO add 404
def main(request):
    return render(request, 'index.html')
