from django.shortcuts import render

from .models import Menu


def index(request):
    categories = Menu.objects.order_by('id').all()
    context = {'categories': categories}
    return render(request, 'app/index.html', context)


def properties(request):
    categories = Menu.objects.order_by('id').all()
    context = {'categories': categories}
    return render(request, 'app/properties.html', context)