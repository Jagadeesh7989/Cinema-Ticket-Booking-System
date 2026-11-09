from movie import Movie, movie


class Booking:
    def __init__(self,customer_name,movie,ticket_count,total_amount):
        self.customer_name=customer_name
        self.movie=movie
        self.ticket_count=ticket_count
        self.total_amount=total_amount

    def caluculate_amount(self):
        return self.ticket_count*self.Movie.ticket_price

    def display_booking(self):
        print(f' ====booking status=====')
        print(f' customer_name : {self.customer_name}')
        print(f' movie name : {self.movie}')
        print(f'ticket count: {self.ticket_count}')
        print(f'total Amount: {self.total_amount}')
        print('='*30)
        print()


movie=Movie('og','telugu','3hrs','250')
# movie.display_movies()
