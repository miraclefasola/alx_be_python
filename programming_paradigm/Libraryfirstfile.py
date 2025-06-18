class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out =  False

    def _str_(self):
        return f"Title: {self.title} by Author: {self.author}"

class Library:
    def _init_(self):
            self._books = []

    def add_book(self, book):

        self._books.append(book)
        print(f"{book} has been added to the library")

    def check_out_book(self,book):

        if book in self._books and book.is_checked_out == False:
            self._books.remove(book)
            print(f"{book} has been checked out")
        elif book not in self._books:
            print(f"{book} does not exist in the library")
        else:
            print(f"{book} has been checked out")

    def return_book(self, title):

        if title not in self._books and title.is_checked_out == True:
            self._books.append(title)
            print(f"{title} has been returned")
        else:
            print(f"{title} exists in the library")
    def list_available_books(self):
        print(f"{self._books}")