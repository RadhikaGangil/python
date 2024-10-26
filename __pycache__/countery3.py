#for example sometimes we may have to make dynamic set
countrylist=set() #this is empty set
while True:
       cname=input("enter the country name")
       countrylist.add(cname)
       answer =input("wnat th add another country name?").upper().strip()
       if(answer=="Y"):
              continue
       else:
              break
print("list of countries")
for x in countrylist:
       print(x)