#***********************Library Management System*************************
class Library:
    def __init__(self,booklist):
        self.AvailableBook=booklist
    def displayAvailableBooks(self):
        print("Books present in library are")
        for books in self.AvailableBook:
            print("*"+books)
    def borrow(self,bookName):
        if bookName in self.AvailableBook:
            print("Your Book is issued")
            self.AvailableBook.remove(bookName)
        else:
            print("Your book is not present or it was taken by someone else")
    def returnBook(self,bookName):
            print("Your book is being returned Successfully")
            self.AvailableBook.append(bookName)
        

class Student:
    def requestBook(self):
        self.book=input("Name the book you want to borrow: ")
        return self.book 
    def returnBook(self):
        self.book=input("Name of the book you want to add/return: ")
        return self.book
        

library=Library(["science","math","pc and clone","Html"])
student=Student()
intro='''
*************Welcome to Student Library******************

             1.Display available books
             2.Add/Return Book
             3.Borrow Book
             4.exit
            '''
print(intro)
while True:
    a=int(input("Enter Your Choice : "))
    if(a==1):
        library.displayAvailableBooks()
    if(a==2):
        library.returnBook(student.returnBook())
    if(a==3):
        library.borrow(student.requestBook())
    if(a==4):
        exit()