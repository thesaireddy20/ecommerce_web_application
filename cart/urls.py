from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_item, name="remove_item"),
    path("checkout/", views.checkout, name="checkout"),  # 🆕 Checkout page
]
