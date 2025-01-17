# your_app/templatetags/cart_tags.py
from django import template
from ..cart import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_item_count(context):
    request = context['request']
    user = request.user
    if user.is_authenticated:
        user_cart = Cart(request)
        cart_len = len(user_cart)
        return cart_len
    return 0
