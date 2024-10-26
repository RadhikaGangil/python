#program for adding two no.
# firstno=input("enter first no.")
# secondno=input("enter other no")
# result=firstno+secondno
# print("total",result)

import datetime

for i in range(7):
    print(datetime.date.today() + datetime.timedelta(days=i))




t1="ajay"
t2="ramesh"
t3="rama"
print("hello",t1,t2,t3,"how you all are")
t1="ekansh"
print("hello",t1,t2,t3,"how you all are")
age=9
print("age is ",age)
age=age+2
print(age)


#program>>3
name=input("enter the name")
age=input("age of person" )
flag="flase"
if(age>=18):
      flag="true"
else:
      flag ="flase"
counter=0
for i in name:
      if(i=='a'):
            counter+=1
if(flag=='true'):
      if(counter>2):
            print("you are lucky")
      else:
            print(" not lucky")




