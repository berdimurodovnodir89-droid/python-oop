class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year


car01 = Car('BMw','x5,',2024)
car02 = Car('GM','damas',2020)

print(car01.brand)
print(car02.model)