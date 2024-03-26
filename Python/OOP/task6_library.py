class Library:
    def __init__(self, name, availableBooks={}, reader={}):
        self.name = name
        self.books = availableBooks
        self.borrowerDetails = reader

    def details(self):
        print(f"{self.name} Library details")
        print(f"Borrower details:\n{self.borrowerDetails}")
        print(f"Books availability:\n{self.books}")


class Reader:
    def __init__(self, name):
        self.name = name
        self.borrowedBooks = {}
        self.bookCount = 0

    def borrow(self, libraryObj, *args):
        for book in args:
            if libraryObj.books[book] > 0 and self.bookCount < 5:
                print(f"{book} book is borrowed successfully.")
                libraryObj.books[book] -= 1
                self.bookCount += 1
                if book in self.borrowedBooks:
                    self.borrowedBooks[book] += 1
                else:
                    self.borrowedBooks[book] = 1

            elif self.bookCount == 5:
                print("You cannot borrow more than 5 books.")
            else:
                print(f"{book} books are not available at the moment.")
        libraryObj.borrowerDetails[self.name] = self.bookCount

    def readerInfo(self, specificBook=""):
        if (specificBook == ""):
            print(f"{self.name}, you have {self.bookCount} book(s) with you")
            for book, number in self.borrowedBooks.items():
                print(f"Books on {book}: {number}")
        else:
            print(
                f"{self.name}, you have {self.borrowedBooks[specificBook]} {specificBook} book(s) with you.")


L1 = Library('Dhaka', {'Arts': 15, 'Fiction': 135,
             'Politics': 2, 'Science': 11, 'Poetry': 15})
L1.details()
print("1----------------------")
r1 = Reader('Aladdin')
r1.borrow(L1, 'Arts', 'Fiction', 'Fiction', 'Politics')
print("2----------------------")
r1.borrow(L1, 'Politics', 'Fiction')
print("3----------------------")
r1.readerInfo()
print("4----------------------")
r1.readerInfo('Fiction')
print("5----------------------")
L1.details()
print("6----------------------")
r2 = Reader('Jasmine')
r2.borrow(L1, 'Politics', 'Poetry')
print("7----------------------")
r2.readerInfo()
print("8----------------------")
L1.details()
