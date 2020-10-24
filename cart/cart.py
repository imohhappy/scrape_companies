from decimal import Decimal
from django.conf import settings
from shopping.models import Shopping
from coupons.models import Coupon


class Chart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session.get[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_id = self.session.get('coupon_id')

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys(self)
        products = Shopping.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(p)]
