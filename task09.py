class User:
    def __init__(self,username,email,is_active):
        self.username = username
        self.email = email
        self.is_active = is_active 
    def activate(self):
        if self.is_active == True:
            print('foydalanuvchi faollashtirildi')
        else :
            print('foydalanuvchi bloklandi')

user01 = User('Nodirbek','nodirbek@gmail.com','is_active')
user02 = User('Dilshod','sultonov@gmail.com','is_active')

user01.activate()
user02.activate()
