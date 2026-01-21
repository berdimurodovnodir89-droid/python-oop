class Movie:
    def __init__(self,title,genre,duration,rating):
        self.title = title
        self.genre = genre 
        self.duration = duration
        self.rating = rating
    def show_summary(self):
        print(f"{self.title } - {self.genre} janridagi film . Reyting : {self.rating}")
        
movie01 = Movie('Avatar','faltastic','1 soat 20 min','4.5/5')
movie02 = Movie('sevgi va dostlik','romantic','1 soat 55 min','9.5/10')

movie01.show_summary()
movie02.show_summary()