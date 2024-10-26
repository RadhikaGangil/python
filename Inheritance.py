#example of inheritnce
class furniture:
       def __init__(x,cl='Brown'):
              x.color=cl
       def InputDeatails(x):
              x.fname=input("enter the name furniture").title().strip()
              x.price=int(input("enter the price"))
              x.material=input("enter material").title().strip()
       def DisplayDetails(x):
              print("furnitue name =%s" %x.fname)
              print("price =%d"%x.price)
              print("material =%s" %x.material)
              print("color =%s"%x.color)
class Chair(furniture):
       def getDetails(x1):
              x1.No_legs=int(input("enter no of legs"))
       def ShowDetails(x1):
             print("deatils")
             super().DisplayDetails()
             print("no of shelf =%d" %x1.No_legs)  
class Almirah(furniture):
       def enterDetails(x1):
              x1.No_shelf=int(input("enter no of legs"))
       def DisplayDetails(x1):
             print("deatils")
             super().DisplayDetails()
             print("no of shelf =%d" %x1.No_shelf)  



class specialfurniture(Chair,Almirah):
       def EnterItemdetails(x1):
              super().InputDeatails()
              super().getDetails()
              super().enterDetails()
       def printDetail(x1):
              super().ShowDetails()
              super().DisplayDetails()         
myalmirah=Almirah()
mychair=Chair()
mychair.InputDeatails()
mychair.getDetails()
mychair.ShowDetails()
myalmirah.InputDeatails()
myalmirah.enterDetails()
myalmirah.DisplayDetails()  #amibugity occuring

specialfurniture1=specialfurniture()
specialfurniture1.EnterItemdetails()
specialfurniture1.printDetail()

