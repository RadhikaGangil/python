#used defined execption >>execption handling
# ANOTHER FORM
answer ="Y"
class SalaryException(Exception):
    pass
while(answer=="y" or answer=="Y"):
    try:
        while(True):
            empname=input("enter the employee name :").upper().strip()
            if(len(empname)==0):
                print("sorry....Emp Name should not be Blank....Try Once Again")
                continue

            else:
              break
        while(True):   
            salary = int(input("enter the salary :"))
            if(salary<25000):
               raise SalaryException()
            else:
                break
        while(True): 
            emailId =input("enter Official Mail ID : ").lower().strip()
            if(not emailId.endswith("@orange.com")):
                print("email id has to be official one..please try again")
                continue
            else:
                break

        print("NAME\t\tSALARY\t\tEMail ID")
        print("*\t\t**\t\t***")
        print("%s\t\t%.2f\t%s" %(empname,salary,emailId))

    except ValueError:
       print("Salary is not proper...please renter")
       continue
    except SalaryException:
        print("Sorry Salary can not be less than 30000")
    except Exception as err1:
        print("Sorry Exception Raised due to ..."+err1)    
    finally:
     print("Thanks")
print("Program Ended Now")