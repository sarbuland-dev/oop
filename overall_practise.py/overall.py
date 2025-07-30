# class person:
#     def __init__(self,name):
#         self.name=name
#     def details(self):
#         print(f"name is {self.name}")

# class book:
#     def __init__(self,book_name,author):
#         self.book_name=book_name
#         self.author=author
#         self.available=True
#     def show(self):
#         if  self.available:
#             status=("available")
#         else:
#             print("not available")
        
#         print(f"book name is {self.book_name}")
#         print(f"author name is {self.author}")
#         print(f"status is {status}")

# class member(person):
#     def __init__(self,name,member_id):
#         super().__init__(name)
#         self.member_id=member_id
#         self.borrow_book=[]
#     def details(self,book):
#         super().details()
#         if book.available:
#             book.available=False
#             self.borrow_book.append(book)
#             print(f"{self.name} borrow a that {book.book_name} book")
#         else:
#             print(f"book unavailable")

# class librarian(person):
#     def __init__(self,name,id):
#         super().__init__(name)
#         self.id=id
#     def add(self,book_list,book):
#         book_list.append(book)
#         print(f"{self.name} added a book {book.book_name}")
#     def remove(self,book_list,book):
#         if book in book_list:
#             book_list.remove(book)
#             print(f"{self.name} remove book {book.book_name}")
#         else:
#             print("book is unavailable")

# book1=book("the love","joneee" )
# book2=book("the hate","robert")
# libaray_book=[book1,book2]
# member1=member("ali",1236712)
# librarian1=librarian("ahmad",123432)
# member1.details(book1)
# new_book=("law of nature","mehar")
# librarian1.add(libaray_book,new_book)
# for b in libaray_book:
#     b.show()


class Person:
    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Name: {self.name}")


class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.available = True

    def show(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book Name: {self.book_name}")
        print(f"Author Name: {self.author}")
        print(f"Status: {status}")


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed the book '{book.book_name}'")
        else:
            print(f"Book '{book.book_name}' is not available.")

    def details(self):
        super().details()
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {[b.book_name for b in self.borrowed_books]}")


class Librarian(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def add(self, book_list, book):
        book_list.append(book)
        print(f"{self.name} added the book '{book.book_name}'")

    def remove(self, book_list, book):
        if book in book_list:
            book_list.remove(book)
            print(f"{self.name} removed the book '{book.book_name}'")
        else:
            print("Book is unavailable")


# Create books
book1 = Book("The Love", "Joneee")
book2 = Book("The Hate", "Robert")

# Book list
library_books = [book1, book2]

# Create member and librarian
member1 = Member("Ali", 1236712)
librarian1 = Librarian("Ahmad", 123432)

# Borrow book
member1.borrow_book(book1)

# Add a new book
new_book = Book("Law of Nature", "Mehar")
librarian1.add(library_books, new_book)

# Show all books
for b in library_books:
    b.show()



        

    

