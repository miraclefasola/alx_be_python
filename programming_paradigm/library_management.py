class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out =  False

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
            self._books = []
    def add_book(self, book):
        self._books.append(book)
        print(f"{book} has been added to the library.")

    def check_out_book(self):
        title = input("Enter the title of the book to return: ")
        for book in self._books:
            if book.title == title:
                if book._is_checked_out == False:
                    book._is_checked_out = True
                    return f"{title} has been checked out"
                else:
                    return f"{title} is already checked out"
        return f"Book {title} is not in the library."



    def return_book(self):
        title = input("Enter the title of the book: ")
        for book in self._books:
            if book.title == title and book._is_checked_out == True:
                book._is_checked_out = False
                print(f"returned {title}.")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        for book in self._books:
            print(f"   {book}")
