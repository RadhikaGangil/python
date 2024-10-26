#file operation
import os 
path="C:\\ITMGWL\\itmgwl.txt"
size=os.path.getsize(path)
print("toatal siize of file =%d bytes" %size)
#codding for calculating lines in a file
fvl=open("C:\\ITMGWL\\itmgwl.txt","r")
data=fvl.read()
print(data)
print("file content shown below")
print(data)
lines=data.split("\n")
print("total no of lines=",len(lines))