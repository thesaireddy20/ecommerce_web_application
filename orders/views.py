# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order, OrderItem
from cart.models import CartItem

# Helper: get all cart items for the logged-in user
def get_cart_items(user):
    return CartItem.objects.filter(user=user)

# Helper: calculate total price of cart items
def calculate_cart_total(user):
    cart_items = get_cart_items(user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return total

# Checkout view
@login_required(login_url='/accounts/login/')
def checkout(request):
    cart_items = get_cart_items(request.user)
    total = calculate_cart_total(request.user)

    if request.method == "POST":
        # Create a new order
        order = Order.objects.create(user=request.user, total=total)

        # Add each cart item as an OrderItem
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity
            )

        # Clear the cart
        cart_items.delete()
        messages.success(request, "Order placed successfully!")
        return redirect('order_success', order_id=order.id)

    return render(request, 'orders/checkout.html', {'cart_items': cart_items, 'total': total})

# Order success view
@login_required(login_url='/accounts/login/')
def order_success(request, order_id):
    # Only allow the user who placed the order to view it
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})

# View to list all orders of the logged-in user
@login_required(login_url='/accounts/login/')
def myorders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/myorders.html', {'orders': orders})
