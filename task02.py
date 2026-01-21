class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade


student01 = Student("Nodirbek",'21 yosh','3-kurs talabasi')
student02 = Student("Aziz",'20 yosh','2-kurs talabasi')

print(student01.name,student01.age,student01.grade)
print(student02.name,student02.age,student02.grade)