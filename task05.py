class Product:
    def __init__(self,name,price,category,in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

produc1 = Product('Non',6000,'non',in_stock=True)
produc2 = Product('Sut',6000,'sut',in_stock=True)

print(produc1.name,produc1.price)
print(produc2.name,produc2.price)