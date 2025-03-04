class Product:
    Discount_rate=0.5
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def discount(self):
        return self.price*(1-self.Discount_rate)
p1=Product("Phone",50000)
p2=Product("Laptop",80000)
print(f"Discounted_price of {p1.name}: {p1.discount()}")
print(f"Discounted_price of {p2.name}: {p2.discount()}")
