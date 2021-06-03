"""
Create a class Book with a parameterised constructor then takes name_of_book, author,
year_of_publish, price_of_book, no_of_copies_available. Create the following methods -
- order_book(no_of_books) : This method should return price of purchase, if no of
books is less than or equal to no_of_copies_available. Else, return “No stock”.
- add_quantity(is_admin, quantity): This method should add quantity of books (2nd
param) to existing no_of_copies_available if is_admin is True and return “Book
quantity updated as <<count>>” . If is_admin is False, return “Unauthorised” as
output.
"""

class Book:
    def __init__(self, name_of_book, author, year_of_publish, prize_of_book, no_of_copies_available):
        self.name_of_book = name_of_book
        self.author = author
        self.year_of_publish = year_of_publish
        self.prize_of_book = prize_of_book
        self.no_of_copies_available = no_of_copies_available
        
    def order_book(self, no_of_book):
        self.no_of_book = no_of_book
        
        if no_of_book <= self.no_of_copies_available:
            self.no_of_copies_available -= no_of_book
            a = self.no_of_book * self.prize_of_book
            return a
        else:
            return "No Stock"
            
    def add_quantity(self,is_admin,quantity):
        self.is_admin = is_admin
        self.quantity = quantity
        
        if is_admin == True:
            b = self.quantity + self.no_of_copies_available
            return "Book quantity updated as {}".format(b)
        else:
            return "Unauthorised"
        
book1 = Book("1stBOOK", "Kira", "2020", 200, 17)

print(book1.order_book(5)) #1000
print(book1.add_quantity(False,17)) #Unauthorised
print(book1.add_quantity(True,17)) #Book quantity updated as 29
