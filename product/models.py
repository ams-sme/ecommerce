class Product():
    pass



class Sales: 
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price


    def price(self):
        print("Price:",self.price)

    def Product_name(self):
        print("Product Name:",self.product_name)


