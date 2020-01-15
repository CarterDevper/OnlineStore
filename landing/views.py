from django.shortcuts import render
from .forms import SubsctiberForm
from products.models import *


def landing(request):
    form = SubsctiberForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])
        print(form)

        new_form = form.save()
    return render(request, 'landing/landing.html', locals())


def home(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())
