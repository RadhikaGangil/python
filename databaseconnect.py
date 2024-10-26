#First Program for Database Connectivity

import sqlite3
try:
    conn = sqlite3.connect('college') #Connection object ,name of database='college'
    cur =conn.cursor()  #Creating the cursor object,processing individual object
    cur.execute("SELECT * FROM Training")
    
    count =0
    print('List of Employee:')
    #print(cur.description)
    for row in cur:
        print(row)
        count+=1
    print("All Rows Displayed")
    print("Total Records = %d" %(count))
    
    cur.execute("select avg(Days) from training")
    for x in cur:
        print("average student training days are")
        print(x)
    
except sqlite3.OperationalError:   #In casw there is connectivity issue
    print("Error...please check table name or database")   
    
except:
    print("Database connectivity Failed...sorry Try Later")
    
finally:
    conn.close()  #closing the connection object
    print("Thanks for using this application")