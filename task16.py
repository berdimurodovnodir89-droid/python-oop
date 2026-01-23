class Book :
    def __init__(self,title,author,is_read = True):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read == True
            
    def status(self):
        if self.is_read :
            print(f' {self.title} kitobi o\'qilgan ')
        else :
            print(f'{self.title} kitobi o\'qimalgan  ')


b01 = Book('otgan kunlar','Abdulla Qodiriy')
b02 = Book('SOS ','jon  Miller')
b03 = Book('Atom  odamlar','james ',False)
b04 = Book('Navoiy  ','oybek ')
b05 = Book('Forsa  ','Umar ',False)

b01.mark_as_read()
b03.mark_as_read()

for i in [b01,b02,b03,b04,b05]:
    if i.is_read :
     i.status()



