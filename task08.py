class Product:
    def __init__(self,name,price,category,in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    def check_stock(self):
        if self.in_stock == True:
            print(f"{self.name} omborda mavjud")
        else :
            print(f"{self.name} omborda mavjud emas ")

produc1 = Product('Non',6000,'non',in_stock=True)
produc2 = Product('Sut',6000,'sut',in_stock=True)

produc1.check_stock()
produc2.check_stock()