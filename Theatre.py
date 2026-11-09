from movie import Movie
# from movie import

class Theatre:


    def __init__(self,theatre_name,movie,total_seats,available_seats):
        self.theatre_name=theatre_name
        self.movie=movie
        self.total_seats=total_seats
        self.available_seats=available_seats


    def display_theatre(self):
        print('\n   theaatre Details  \n')
        print(f'theatre name: {self.theatre_name}')
        print(f'movie: {self.movie}')
        print(f'total seats: {self.total_seats}')
        print(f'available seats: {self.available_seats}')
        print('='*30)

    def check_availability(self):
        print(f' Available seats: {self.available_seats}')

    def book_ticket(self,quantity):
        if quantity<=0:
            print('invalid Seats')
            return False
        elif quantity>self.available_seats:
            print('seats are not available')
            return False
        self.available_seats-=quantity
        print('successfully booked')
        print('='*30)
        print()
        return True

    def cancel_ticket(self,quantity):
        if quantity<=0:
            print('invalid Seats')
            return False
        elif quantity >= self.available_seats - self.total_seats:
            print('seats are not available')
            return False
        elif 0<quantity<=self.total_seats-self.available_seats:
            self.available_seats+=quantity
            print('successfully Tickets canceled')
            return True
        else:
            print('Invalid Quantity')
            return False


movie=Movie('og','telugu','3hrs','250')

theatre=Theatre('multiplex','OG',300,90)
# theatre.display_theatre()
# theatre.book_ticket(4)
# theatre.cancel_ticket(2)
