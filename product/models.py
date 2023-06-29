class Product():
    pass

class Sales: 
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price


    def show_price(self):
        print("Price:",self.price)

    def show_product_name(self):
        print("Product Name:",self.product_name)


