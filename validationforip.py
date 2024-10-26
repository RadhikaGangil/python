#validation for ip address
import ipaddress
try:
       pp=ipaddress.ip_address(input("enter valid address"))
       print("ip address obtained"+str(pp))
       col=str(pp).split(".")
       print("list of octal are")
       for x in col:
            print(x)
except:
       print("invalid inpput")
#        serverip=input("enter ip addres").strip()
#        octalist=serverip.split(".1")
# print("octal are")
# for x in octalist:
#        print(x)