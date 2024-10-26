#for find sq.root no
#import =for importing module
#%.2f is used for printing any value in specfic limit

# import math
# myno=int(input("enter no"))
# result=math.sqrt(myno)
# print(f'sq.root{myno} is %.2f' %result)
# print("sq.root of %d is %.2f"%(myno,result))


#p>>>2ṇ
#for print  the temp into celsius

# import math
# celsiustemp=float(input("enter the temperature in celsius"))
# result=(((9/5)*celsiustemp)+32)
# print("temp in fahernite is %.2f id %f" %(result,celsiustemp))


#p>>3
#to input a no and check the disible by 5 and 8
#we can also use elif statements

# myno=int(input("enter your no"))
# result1=myno %5
# result2=myno %8
# if(result1==0 and result2==0):
#     print("%d is divisilbe by both 5 and 8" %myno)   
# if(result1!=0 and result2==0):
#     #elif is also used
#     print("%d is divisilbe by 8 and not by 5" %myno)
# if(result1==0 and result2!=0):
#     print("%d is divisilbe by  5 and  not by 8" %myno)
# if(result1!=0 and result2!=0):
#     print("%d is not divisilbe by both 5 and 8" %myno)

# print("program ended")       


# p>>>4lab exercise
answer="Y"
while True:
    
  empname=input("enter the employee name :").upper().strip()
  if(len(empname)==0):
     print("sorry emp name should not be blank ...try once agian")
  else:
    print("salary getting processed")
    break
while True:
  
  salary=int(input("enter the salary: "))
  salary=int (input("enter the salary:"))
  if(salary>=25000):
    break
  else:
    print("improper salary..")
    continue
while True:
  
 emailid=input("enter the emailid :").lower().strip()
 if(len(emailid)==0 or not emailid.endswith("itmgoi.in")):
   print("not a vaild emailid")
   continue
 else:
   break
print("NAME\t\tSALARY\t\tEMAIL ID")
print("*****\t\t*****\t\t*******")
print(empname+"\t\t"+"%.2f\t%s" %(salary,emailid))

print("salary slip generate")



#p>>>>5
#mystr="Python TRAiniNG"
#my="radhika"
# print(mystr[0:4])
# print(mystr[-5:-1])
# print(mystr[:-3])
# print(my[len(my)-3:])
# print(my[::-1])#for reverse the string
# print(my[-1:-3])
#print(mystr[len(mystr)-3:])



#p>>6 plaindrome of a no
#Kanak -is also not a palindrom bcz k is captial
# for removing space use strip method  


# my="kanak"
# mii=my[::-1]
# print(mii)
# if (my==mii):
#   print("palindrome")
# else:
#   print("not")  
 

 #p>>>7 for enter words and calculate the no. words
# str=input("enter the senteces").split(" ")
# print(str)



#p>>8 program
# circuitid="LON/LON/LE123456"
# parts=circuitid.split("/")
# newcircuitid=parts[2]
# newcircuitid=newcircuitid[:2]+"XXX-"+newcircuitid.split("-")[1]
# print(newcircuitid)
# print("encrypted id =",parts[0]+"/"+parts[1]+"/"+newcircuitid)


#p>>>8 using of find function  
#declarea variable
quote="Irrational lenders came and go --mostly they go"
#find a word with no start and end argumnt
print(quote.find("and"))


#p>>>>9
mystatement="Python training is going on.It is a useful training program.it is easy to lraen as well".split() 
print(mystatement)
