from django.shortcuts import render

# TODO add 404
def main(request):
    return render(request, 'index.html')
