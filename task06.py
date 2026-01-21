class Student:
    def __init__(self,ism,yosh,sinf):
        self.name = ism 
        self.age = yosh
        self.clas = sinf
    def shov_info(self):
        print(f' {self.name} {self.age} yoshda {self.clas} sinfda ')



s01 = Student(ism = 'ali', yosh = 13 , sinf = 6)
s02 = Student(ism = 'vali', yosh = 12 , sinf = 5)
s03 = Student(ism = 'sami', yosh = 14 , sinf = 7)

for i in [s01,s02,s03]:
    i.shov_info()

    
    