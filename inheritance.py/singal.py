class Book:
    def __init__(self,name,author,stock):
        self.name=name
        self.author=author
        self.stock=stock
    def __str__(self):
        return(f"Book name is {self.name} and author is {self.author} and stock remain are {self.stock}")
    
    
class Ebook(Book):
    def __init__(self,name,stock,author,file_format,download_link):
        super().__init__(name,stock,author)
        self.file=file_format
        self.link=download_link
    def show(self):
        print(f"your book details are ")
        print([{"name":self.name,"Author":self.author,"stock":self.stock,"file format":self.file,"download link":self.link}])
 
s1=Ebook("the love","jon",34,"PDF","htp//user//download//.com")
s1.show()