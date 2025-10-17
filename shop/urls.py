from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop_home'),  # homepage
    path('category/<slug:slug>/', views.category_view, name='category_view'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search_view, name='search_view'),
]
