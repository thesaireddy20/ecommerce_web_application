from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from shop.models import Product
from django.contrib.auth.decorators import login_required


# ➕ Add product to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:
        return redirect("login")  # force login before adding
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect("view_cart")


# 🛒 View cart
def view_cart(request):
    if not request.user.is_authenticated:
        return redirect("login")
    items = CartItem.objects.filter(user=request.user)
    total = sum([it.product.price * it.quantity for it in items])
    return render(request, "cart/cart.html", {"items": items, "total": total})


# ❌ Remove item from cart
def remove_item(request, item_id):
    it = get_object_or_404(CartItem, id=item_id, user=request.user)
    it.delete()
    return redirect("view_cart")


# ✅ Checkout (Login Required)
@login_required
def checkout(request):
    items = CartItem.objects.filter(user=request.user)
    if not items:
        return redirect("view_cart")  # no items to checkout

    total = sum([it.product.price * it.quantity for it in items])

    # In a real system you would create an order here
    # For now, just show confirmation
    return render(
        request,
        "cart/checkout.html",
        {"items": items, "total": total},
    )
