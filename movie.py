class Movie:


    def __init__(self,movie_name,language,duration,ticket_price):
        self.movie_name=movie_name
        self.langauge=language
        self.duration=duration
        self.ticket_price=ticket_price


    def display_movies(self):
        print(f'Movie Name: {self.movie_name}')
        print(f'langage: {self.langauge}')
        print(f'duration: {self.duration}')
        print(f'ticket price: {self.ticket_price}')
        print('='*20)


movie=Movie('og','telugu','3hrs','250')

# movie.display_movies()
