#Assignment 2
#u are suppossed to enter the details of some item like 
# itemname,qty,price

# qty &price can not be 0 or -ve ,in case you enter any such  you enter anny value then immedatialy wrongvalueError (an user defined exception should be generated)
  

answer='Y'
class WrongValueError(Exception):
       
       pass
class PriceError(Exception):
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
              while(True):
                    price=int(input("enter the price"))
                    if(price<=0):
                     raise PriceError()
                    else:
                        break
                     

                     


  except WrongValueError:
         print("quantity not in negetive")
  except PriceError:
        print(" price can not be negetive")       
  finally:
         print(" this is last line of program")
         
         