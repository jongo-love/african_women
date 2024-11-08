# ecommerce/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='ecommerce/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='ecommerce/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]
