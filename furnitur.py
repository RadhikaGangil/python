# You have to create a class furniture which contains following information
#furniurename,color,material,price.IMPLEMENT 2 member function getdetail ND DISPLAYDETAL TO ENTER AND SHOW ABOVE INFORMATION.
#IMPLEMNT CONSTRUCTOR AND IINITILAIZE MATERILA AS WOODEN
#also count code to check and count no of records
class Furniture:
    def _init_(myself,mat="Wooden"): # parameterized constructor---
        myself.material=mat
    def GetDetail(myself):
        myself.fname=input("Enter furniture name\n")
        myself.color=input("Enter color")
       # myself.material=input("Enter material")
        myself.price=int(input("Enter price"))
    def DisplayDetail(myself):
        print("Furniture name=",myself.fname)
        print("Furniture color=",myself.color)
        print("Furniture material=",myself.material)
        print("Furniture price=",myself.price)
    def StoreFile(myself):
        fv1=open("D:\\chatboat\\chatbot\\b.Csv","a")
        data=myself.fname+","+myself.color+","+str(myself.price)+","+myself.material+","+"\n"
        fv1.write(data)
        print("record added successfully")
        fv1.close()
    def CountLine(myself):
        fv1=open("D:\\chatboat\\chatbot\\b.Csv","r")
        data=fv1.read()
        lines=data.split("\n")
        print("total lines",len(lines )-1)
        fv1.close()
fur1=Furniture()
fur1.GetDetail()
fur1.DisplayDetail()
fur1.StoreFile()
fur2=Furniture()
fur2.GetDetail()
fur2.DisplayDetail()
fur2.StoreFile()
fur2.CountLine()