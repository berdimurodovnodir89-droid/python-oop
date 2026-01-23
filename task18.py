class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category

    def info(self) :
        return f"Eng qimmat elektronika: {self.name} {self.price} so\'m "
    
Products = [
    Product('S25',900,'Elektronika'),
    Product('iphone 15 pro',900,'Elektronika'),
    Product('HP',700,'Elektronika'),
    Product('Pixel',800,'Elektronika'),
    Product('Mi',200,'Elektronika'),
    Product('Honor',400,'Elektronika'),
]
max_price = max(Products,key=lambda produc: produc.price)
print(max_price.info())

