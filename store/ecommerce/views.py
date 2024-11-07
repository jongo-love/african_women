from django.shortcuts import render,get_object_or_404
from .models import Product, Category
# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'ecommerce/product_list.html', context)

# ecommerce/views.py
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    context = {'product': product}
    return render(request, 'ecommerce/product_detail.html', context)
