#you have to create class say furniture which cotains the following info
#furnituename,color,material, price
#implement 2 member function-getdetails(),and displaydetails()to enter show info
#implement constructor and intailze materail as wooden
import os
get_file_size=lambda file_path:os.path.getsize(file_path) if os.path.exists(file_path) else 0
class Furniture:
       def __init__(myself):
               myself.material="Wooden"
       def GetDetails(myself):
              myself.furniturename=input("enter furniture name").upper().strip()
              myself.color=input("enter the color").upper().strip()
              #myself.material=input("enter the material").upper().strip()
              myself.price=int(input("enter the price"))
       def DisplayDetails(myself): 
              print("furnitue name =",myself.furniturename)
              print("furnitue color =",myself.color)
              print("furniture material=",myself.material)
              print("price=",myself.price)
       def StoreFile(myself):
              fv1=open("C:\\ITMGWL\\itmgwl.Csv","a") 
              data=myself.furniturename+","+myself.color+","+str(myself.price)+","+myself.material+","+"\n"
              fv1.write(data)
               
              print("Recorded Added Successfully")
              fv1=open("C:\\ITMGWL\\itmgwl.Csv","r") 
              data=fv1.read()
              lines=data.split("\n")
              print("total no of lines=",len(lines)-1)
              path="C:\\ITMGWL\\itmgwl.txt"
              size=os.path.getsize(path)
              print("toatal siize of file =%d bytes" %size)      
              fv1.close()
              size =get_file_size("C:\\ITMGWL\\Furniture.Csv") 
              print(size)

       # def CountLine(myself):
       #        fv1=open("C:\\ITMGWL\\itmgwl.Csv","r") 
       #        data=fv1.read()
       #        lines=data.split("\n")
       #        print("total no of lines=",len(lines)-1)   
       #        fv1.close()  
               
Furniture1=Furniture()
Furniture1.GetDetails()
Furniture1.DisplayDetails()
Furniture1.StoreFile()
#Furniture1.CountLine()

#Assignment 2
#u are suppossed to enter the details of some item like 
# itemname,qty,price

# qty &price can not be 0 or -ve ,in case you enter any such  you enter anny value then immedatialy wrongvalueError (an user defined exception should be generated)
  

answer='Y'
class WrongValueError(Exception):
       
       pass
while(answer=="y" or answer=="Y"):
  try:
              while(True):
                     itemName=input("enter the name of item").upper().strip()
                     if(len(itemName)==0):
                            print(" item name is must")
                            continue
                     else:
                         break

              while(True):
                     quantity=int(input("enter the quantity of item"))
                     if(quantity<=0):
                         raise WrongValueError()
                            
                     else:
                            break


  except WrongValueError:
         print("quantity not in negetive")
  finally:
         print(" this is last line of program")
         
         