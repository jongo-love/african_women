from django.shortcuts import render,get_object_or_404
from .models import Product, Category
from .forms import UserRegistrationForm
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


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ecommerce:product_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'ecommerce/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def admin_dashboard(request):
    if request.user.is_staff:
        # Redirect to Django's default admin panel
        return redirect('/admin/')
    else:
        return HttpResponseForbidden("You do not have access to this page.")