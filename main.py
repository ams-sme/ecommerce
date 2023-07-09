import csv
from datetime import date, timedelta

class Book:
    def __init__(self, book_id, title, author,quantity):
        self.book_id = book_id
        self.title = title 
        self.author = author
        self.quantity = quantity

    def display_info(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Quantity : {self.quantity}")

    def update_quantity(self,new_quantity):
        self.quantity = new_quantity

class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name

    def display_info(self):
        print(f"Borrower ID : {self.borrower_id}")
        print(f"Name : {self.name}")


class Transaction:
    def __init__(self, book, borrower, borrow_date):
        self.book = book
        self.borrower = borrower
        self.borrow_date = borrow_date
        self.expected_return_date = borrow_date + timedelta(days= 15)
        self.actual_return_date = None

    def display_info(self):
        print("Transaction Details :")
        print("-----------------------")
        self.book.display_info()
        self.borrower.display_info()
        print(f"Borrow Date : {self.borrow_date}")
        print(f"Expected Return Date : {self.expected_return_date}")
        if self.actual_return_date:
            print(f"Actual Return Date : {self.actual_return_date}")

class LMS:
    def __init__(self):
        self.book = []
        self.borrowers = []
        self.transactions = []

    def load_book_from_csv(self,file_path):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                book_id, title, author, quantity = row
                book = Book(book_id, title, author, int(quantity))
                self.books.append(book)

    def add_book(self,book):
        self.books.append(book)
    
    def remove_book(self,book_id):
        for book in self.books:
            if book.book_id ==book_id:
                self.books.remove(book)
                break
    
    def update_book_quantity(self,book_id, new_quantity):
        for book in self.books:
            if book.book_id == book_id :
                book.update_quantity(new_quantity)
                break 

    def display_all_book(self):
        for book in self.books:
            book.display_info()
            print("---------------")

    def add_borrower(self,borrower):
        self.borrowers.append(borrower)

    def remove_borrower(self, borrower_id):
        for borrower in self.borrowers:
            if borrower.borrower_id == borrower_id:
                self.borrowers.remove(borrower)
                break
            
    def display_all_borrowers(self):
        for borrower in self.borrowers:
            borrower.display_info()
            print("------------------------")

    def borrow_book(self,book_id,borrower_id):
        book = self.find_book_by_id(book_id)
        borrower = self.find_borrower_by_id(borrower_id)

        if not book or not borrower:
            print("Invalid book ID or borrower ID. ")
            return
        
        if book.quantity > 0:
            transaction = Transaction(book, borrower, date.today())
            self.transactions.append(transaction)
            book.update_quantity(book.quantity - 1)
            print("Book borrowed successfully. ")
        else:
            print("Book not available. ")

    def return_book(self,book_id):
        for transaction in self.transactions:
            if transaction.book.book_id == book_id and not transaction.actual_return_date:
                transaction.actual_return_date = date.today()
                transaction.book.update_quantity(transaction.book.quantity + 1)
                print("Book returned successfully.")
                return
        print("invalid book ID or book already return. ")
    
    def find_book_by_id(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    
    def find_borrower_by_id(self,borrower_id):
        for borrower in self.borrowers:
            if borrower.borrower_id == borrower_id:
                return borrower
        return None

def display_menu():
    print("1. Display all Books.")
    print("2. Display all borrowers.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Exit.")

def main():
    library = LMS()
    library.load_book_from_csv("books.csv")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_all_book()
        elif choice == "2":
            library.display_all_borrowers()
        elif choice == "3":
            book_id = input("Enter the book ID: ")
            borrower_id = input("Enter the borrower ID :")
            library.borrow_book(book_id,borrower_id)
        elif choice == "4":
            book_id = input("Enter the book ID: ")
            library.return_book(book_id)
        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid choice. Please try again.")
            print("Yes")

if __name__ == "__main__":
    main()


        
