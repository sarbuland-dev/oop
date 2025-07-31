# class Person:
#     def __init__(self, name):
#         self.name = name

#     def details(self):
#         print(f"Name: {self.name}")


# class Book:
#     def __init__(self, book_name, author):
#         self.book_name = book_name
#         self.author = author
#         self.available = True

#     def show(self):
#         status = "Available" if self.available else "Not Available"
#         print(f"Book Name: {self.book_name}")
#         print(f"Author Name: {self.author}")
#         print(f"Status: {status}")


# class Member(Person):
#     def __init__(self, name, member_id):
#         super().__init__(name)
#         self.member_id = member_id
#         self.borrowed_books = []

#     def borrow_book(self, book):
#         if book.available:
#             book.available = False
#             self.borrowed_books.append(book)
#             print(f"{self.name} borrowed the book '{book.book_name}'")
#         else:
#             print(f"Book '{book.book_name}' is not available.")

#     def details(self):
#         super().details()
#         print(f"Member ID: {self.member_id}")
#         print(f"Borrowed Books: {[b.book_name for b in self.borrowed_books]}")


# class Librarian(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id

#     def add(self, book_list, book):
#         book_list.append(book)
#         print(f"{self.name} added the book '{book.book_name}'")

#     def remove(self, book_list, book):
#         if book in book_list:
#             book_list.remove(book)
#             print(f"{self.name} removed the book '{book.book_name}'")
#         else:
#             print("Book is unavailable")


# # Create books
# book1 = Book("The Love", "Joneee")
# book2 = Book("The Hate", "Robert")

# # Book list
# library_books = [book1, book2]

# # Create member and librarian
# member1 = Member("Ali", 1236712)
# librarian1 = Librarian("Ahmad", 123432)

# # Borrow book
# member1.borrow_book(book1)

# # Add a new book
# new_book = Book("Law of Nature", "Mehar")
# librarian1.add(library_books, new_book)

# # Show all books
# for b in library_books:
#     b.show()


# class rider:
#     def __init__(self,name):
#         self.name=name
#         self.current_ride=None
#     def rider_request(self,pickup,dropup):
#         if self.current_ride:
#             print("you already in a ride")
#             return None
#         ride=Ride(self,pickup,dropup)
#         self.current_ride=ride
#         return ride
    
# class driver:
#     def __init__(self,name):
#         self.name=name
#         self.current_ride=None
#     def accept_request(self,ride):
#         if self.current_ride:
#             print("your are already in a ride")
#             return 
#         if ride.status!="Requested":
#             print("ride is not available")
#             return
#         ride.driver=self
#         ride.status="Accepted"
#         self.current_ride=ride
#         print(f"{self.name} accept your request")

# class Ride:
#     def __init__(self,rider,pickup,dropup):
#         self.rider=rider
#         self.driver=None
#         self.pickup=pickup
#         self.dropup=dropup
#         self.status="Requested"
#     def complete(self):
#         if self.status!="Accepted" :
#          print("ride is not in progress")
#          return  
#         self.status ="Complete"
#         print("ride is completed")
#     def cancle(self):
#           if self.status == "Completed":
#             print("Cannot cancel a completed ride.")
#             return
#           self.status = "Cancelled"
#           print("Ride cancelled.")

# r=rider("ali")
# d=driver("ahmad")
# ride=r.rider_request("muslim town","thokar naiz biag")
# d.accept_request(ride)
# ride.complete()


class animal:
    def speak(self):
        print("diferent animal")

class lion(animal):
    def speak(self):
        print("rorr")

class sanak(animal):
    def speak(self):
        print("snnnnsnsnsn")

class elephant(animal):
    def speak(self):
        print("uuuuuhuuu")

s1=lion()
s1.speak()
        


        

    

