#program ofclass and object  >>>>> BOOK class
#member variable 2.member function
class Book:
       # def __init__(myself):
       #        myself.price=123
       # def __init__(myself):  # default constructor
       #        myself.pubname="Rupa Publishers"
       
       def __init__(myself,pname="Rupa Publishers"):  # parameterize constructor
              
              myself.pubname=pname
       def EnterDetail(myself):# member function1
              status="Book Details" #local variable
              myself.bookname=input("enter book name").upper().strip() #bookname=member variable
              myself.authorname=input("enter author name").upper().strip()
              myself.price=int(input("enterprice"))
              myself.pagesno=int(input("enter pagesno"))
              #myself.pubname=input("enter pubname").upper().strip()

       def ShowDetails(myself):    # member function2
              print("bookname=",myself.bookname)       
              print("authorname=",myself.authorname)       
              print("price=",myself.price)  
              print("pagesno=",myself.pagesno)       
              print("pubname=",myself.pubname)      
       def StoreFile(myself):
              try:
               fv1=open("C:\\ITMGWL\\itmgwl.txt","a")
               data=myself.bookname+","+myself.authorname+","+str(myself.price)+","+myself.pubname+","+str(myself.pagesno)+"\n"
               fv1.write(data)
               print("Recorded Added Successfully")
               fv1.close()
              except PermissionError:
                    print("sorry premission  denied")

              except FileNotFoundError:
                    print("sorry please check file path")
              finally:
                    print("file processed")       
            

class Syllabus(Book):
      
      
Book1=Book() #object creating
Book1.EnterDetail()  #book.enterdeatail(book1)
Book1.ShowDetails()
Book1.StoreFile()

Book2=Book("pengunie publisher")
Book2.EnterDetail()
Book2.ShowDetails()
Book2.StoreFile()


