class Book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_read = False

    def mark_as_read(self):
        self.is_read == True
            
    def status(self):
        if self.is_read :
            print('Kitob o\'qilgan ')
        else :
            print('Kitob o\'qimalgan  ')


b01 = Book('otgan kunlar','Abdulla Qodiriy')
b02 = Book('SOS ','jon  Miller')
b03 = Book('Atom  odamlar','james ')
b04 = Book('Navoiy  ','oybek ')

b01.mark_as_read()
b03.mark_as_read()

b01.status()
b02.status()
b03.status()
b04.status()

