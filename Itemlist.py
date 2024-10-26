import sqlite3
conn= sqlite3.connect('college')
cur=conn.cursor()
cur.execute("SELECT * FROM ItemList")
mini=cur.execute("Select min(price) from ItemList")


for x in mini:
    print("The minimum is ",x)
maxi=cur.execute("Select max(price) from ItemList")
for x in maxi:
    print("The maximum is ",x)
for x in maxprice:
    