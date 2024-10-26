#for example sometimes we may have to make dynamic list
countrylist=[] #this is empty list
while True:
       cname=input("enter the country name")
       countrylist.append(cname)

       answer=input("want th add another country name?").upper().strip()
       if(answer=="Y"):
              continue
       else:
              break
print("list of countries")
for x in countrylist:
       print(x)
# x.split()
# print(x)