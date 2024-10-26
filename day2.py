# # p>>1  list program
# techcourses=["power bi","AWS","MS sQL SERVER","Python","Github"]
# ecourses=["soft skills","project management","crisis managgament","customer handling"]
# #we combine both the list ---concatinate
# allcourses=techcourses+ecourses
# #print(allcourses)
# #second way of repersentaion
# allcourses.sort() #sorting
# allcourses.append("cybersercuity") #append insert at last
# allcourses.insert(0,"snowflakes")#insert at any particular index
# allcourses.remove("Github")#remove any element
# for x in allcourses:     #x is a itrator ,in is a membership operator
#    print(x)

# print("total courses :", len(allcourses))
# course=[]
# for x in allcourses:
#    course.append(x.upper())
# #script to search a particular course

# ename=input("enter a couses to search ?").upper().strip()
# if ename in course:
#    print("%s is available in the list" %ename)
# else:
#    print("%s is not available in the list " %ename)   
# #to remove any variable from the memory
# del techcourses,allcourses


#p>>>2
webinarlist=["milan@rafs","milan@orange.com","radah@mkn","vssyg@nn","bjhbb@bnzbc","orange.ocm","shehh@ds"]
orangelist=[]
outsider=[]
for x in webinarlist:
   if(x.endswith("@orange.com")):
      orangelist.append(x)
   else:
      outsider.append(x)
print("people attended from orange")
print(orangelist)
print("people from outsider orange")
print(outsider)   

# p>>3  progrm of tuple
stationlist=("gwalior","jhansi","vidisha","bina","bhopal","habibganj")
print(stationlist)
#now we convert it into list by using list keyword
target=list(stationlist)
print(target)
target.pop(4)
target.append("rani kamlapati")
print(target)
#convert it into again into tuple
stationlist=tuple(target)
print(stationlist)

#p>>4
vegetable=["potato","tomato","brinjal","cauliflower","beans","beans","brinjal","onion"]
#now convert it into set
veg=(list(vegetable))
print(veg)
veg.sort()
print(veg)


convertset=set(vegetable)

print(convertset)



#p>>>5   program o using set
import pandas as pd  #pd is konow as alias name of pandas
from collections import Counter #import k bad module ka nam ayaga  counter is known as module

vegetable=["potato","tomato","brinjal","cauliflower","beans","beans","brinjal","onion"]
#dataframe works as distribute into rows and column
mydata=pd.DataFrame.from_dict(Counter(vegetable).items())

print(mydata)




#operation on set p>>>6
pricorus={"sales","IT","CSO","FSO","LDM"}
symphony={"sales","CSO","purchase","HR","admin"}
#symnphony has process pricorous
newdepts=pricorus-symphony # -finding a difference
print("new depts to be formed")
print(newdepts)
print("total new depts =%d" %(len(newdepts)))


cdept=pricorus &symphony # & stands for intersection
print("common depts to be formed")
print(cdept)
print("total commom depts =%d"%(len(cdept)))

#ow to combine both these sets --  "| union process"
overalldept=pricorus|symphony
print("overall depts to be formed")
print(overalldept)
print("total common depts =  %d"%len(overalldept))


#p>>>8
country_name="INDIA"
myit=iter(country_name)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#factorail
def factorail(n):
   #base case :if n is 0,return1
   if n==0:
      return 1
   #recursive case:n*factoaril of(n-1)
   else:
      return n* factorail(n-1)
print(factorail(5))