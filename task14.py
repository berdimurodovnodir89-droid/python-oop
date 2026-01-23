class Student:
    def __init__(self,ism,yosh):
        self.name = ism 
        self.age = yosh

    def shov_info(self):
        print(f'Students {self.name} {self.age} yoshda ')


students = [

    Student('Ali', 13 ),
    Student('Vali',  12 ),
    Student('Sami',  14 ),
    Student('Soli',16 ),
    Student('Jami',  11 )
]
student = max(students,key=lambda student : student.age)
student.shov_info()
    
    