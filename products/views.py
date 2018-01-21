from django.shortcuts import render
from products.models import Product
from django.contrib.auth.decorators import login_required


@login_required
def all_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})