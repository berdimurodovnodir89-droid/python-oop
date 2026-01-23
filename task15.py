class Product:
    def __init__(self,name,price,in_stock = False):
        self.name = name 
        self.price = price
        self.in_stock = in_stock
    

Products = [
    Product('S23',700,True),
    Product('S25',900),
    Product('iphone 15 pro',750),
    Product('pixel',900,True)
]

total = sum(map(lambda Product :Product.price if Product.in_stock else 0 ,Products))
print(F"Ombordagi mahsulotlar narxi:{total}")