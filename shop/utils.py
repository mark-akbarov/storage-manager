from django.shortcuts import get_object_or_404

from .models import Product


def calculate_remaining(product_pk: int):
    """Utility function to calculate remaining products in stock"""
    product = get_object_or_404(Product, pk=product_pk)
    sold_quantity = sum([i.quantity for i in product.order_items.all()])
    product.remaining_quantity = product.total_quantity - sold_quantity
    return product.remaining_quantity
