from decimal import Decimal

from products.models import Product

class Cart:
    def __init__(self, request):

        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
            cart = self.session.get('cart')

        self.cart = cart


    def save(self):
        self.session.modified = True    


    def add(self, product, quantity=1, override_quantity=False):
        product_id_str = str(product.id)

        if product_id_str not in self.cart:
            self.cart[product_id_str] = {'quantity' : quantity}
        if override_quantity:   
            self.cart[product_id_str]['quantity'] = quantity
        else:
            self.cart[product_id_str]['quantity'] += quantity

        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item    


    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_sub_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item
                in self.cart.values())
        
    def clear(self):
        for key in list(self.cart.keys()):
            del self.cart[key]   

        self.save()     
