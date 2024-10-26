#execption handling value error is occur 
#try  except  finally
try: 
 firstno=int(input("enter the first no"))
 secondno=int(input("enter the second no"))
 result=firstno/(secondno-3)
 print(result) 
except ValueError: # valueerror -known as ececption classes ,these all are class name
 print("input data should be number only .. enter correct data")
except ZeroDivisionError:
 print("division by 0 is not possible")
except Exception as K:
 print("sorry ...execption raised ..."+K) 
finally:
 print("thanks ....program ended")