# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print(f"Book with ID {self.bid} is being deleted.")

    def show_book(self):
        print(f"Book ID: {self.bid}")
        print(f"Book Name: {self.bname}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")