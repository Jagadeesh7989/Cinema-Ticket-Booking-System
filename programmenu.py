
from movie import Movie
from Theatre import theatre, movie
from booking import Booking
class Program:
     def display_menu(self):
         while True:

             print(f'1. display Movie ')
             print(f'2. Display Theatre')
             print(f'3. check Availabilty')
             print(f'4. book tickets')
             print(f'5. cancel tickets')
             print(f'6.exit')
             ch = int(input('enter the choice'))
             if ch==1:
                 Movie.display_movies(movie)
             elif ch==2:
                 theatre.display_theatre()
             elif ch==3:
                 theatre.check_availability()
             elif ch==4:
                 name=input('enter the name')
                 ticket_count=int(input('enter the number of tickets'))
                 if theatre.book_ticket(ticket_count):
                     cus=Booking(customer_name,movie,ticket_count)
                     cus.display_booking()
                     print('=' * 30)
                     print()
             elif ch==5:
                 theatre.cancel_ticket(quantity)
                 print('=' * 30)
                 print()
             elif ch==6:
                 break

menu=Program()
menu.display_menu()