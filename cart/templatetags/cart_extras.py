from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies value by arg"""
    return value * arg
