class Movie:
    def __init__(self,title,genre,duration,rating):
        self.title = title
        self.genre = genre 
        self.duration = duration
        self.rating = float(rating)

movie01 = Movie('Avatar','faltastic','1 soat 20 min',9.5)

print(movie01.title,movie01.genre,movie01.duration,movie01.rating)