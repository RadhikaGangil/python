import sqlite3    # this module will only work for sqlite
try:
       conn=sqlite3.connect('college')   #connection with database
       cur=conn.cursor() # adding  a record  in employee table
       Tcode=input("enter training code :").strip()
       Tname=input("enter training name:").title().strip()
       NoDays=int(input("enter dept.no"))
       remarks=input("enter remarks").strip().title()
       sqlstatement=("insert into training values(?,?,?,?)") #?for parameters
       mytuple=(Tcode,Tname,NoDays,remarks)
       cur.execute(sqlstatement,mytuple)
       conn.commit()   # then only record will be saved within the table
       print("record successfully added")
except sqlite3.OperationalError:
       print("soory database connectivity failed")
except sqlite3.IntegrityError as err:
       print("some critria not filled")
       print(err)
except Exception as e:
       print(e)
       print("record could not be added")
finally:
       print("program ended")

  