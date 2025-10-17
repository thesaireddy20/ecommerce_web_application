from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# 🏠 Homepage - show categories and some products
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:24]   # show first 24 products
    return render(
        request,
        "shop/home.html",
        {"categories": categories, "products": products},
    )


# 📂 Products under a category
def category_view(request, slug):
    categories = Category.objects.all()
    cat = get_object_or_404(Category, slug=slug)
    products = cat.products.all()
    return render(
        request,
        "shop/category.html",
        {"categories": categories, "products": products, "current": cat},
    )


# 📦 Product details
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.all()
    return render(
        request,
        "shop/product_detail.html",
        {"product": product, "categories": categories},
    )


# 🔍 Search products
def search_view(request):
    q = request.GET.get("q", "")
    categories = Category.objects.all()
    products = (
        Product.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if q
        else Product.objects.none()
    )
    return render(
        request,
        "shop/search.html",
        {"categories": categories, "products": products, "query": q},
    )


# 🆕 Register new user
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
