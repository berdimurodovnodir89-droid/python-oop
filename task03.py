class User:
    def __init__(self,username,email,is_active):
        self.username = username
        self.email = email
        self.is_active = is_active 

user01 = User('Nodirbek','nodirbek@gmail.com','is_active')
user02 = User('Dilshod','sultonov@gmail.com','is_active')

print(user01.username,user01.email,user02.is_active,False)
print(user02.username,user02.email,user02.is_active ,True)
