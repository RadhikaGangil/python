import pandas as pd
import math
mydata = pd.read_excel("C:\\Users\\Dell\\Downloads\\loan.xls")
print(mydata)
#using python script find out the maxmimum loan amount,average loan amount ,min
MYMAX=mydata['Loan Amount'].max()
MYMIN=mydata['Loan Amount'].min()
MYAVG=mydata['Loan Amount'].mean()
print(f"{MYMAX}")
print(f"{MYMIN}")
print(f"{MYAVG}")
# cours       ename=set(mydata["course"])
# print(coursename)


