import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("example of treeveiw")
root.geometry("400x200")

tree=ttk.Treeview(root)
tree.pack()

master_item=tree.insert("","end","master_item",text="master Item")
#add item enter master item
item1=tree.insert(master_item,"end","item1",text="item 1")
item2=tree.insert(master_item,"end","item2",text="item 2")
item3=tree.insert(master_item,"end","item3",text="item 3")

#add subitem for item1
tree.insert(item1,"end","subitem1_1",text="subitem1.1")

tree.insert(item1,"end","subitem1_2",text="subitem1.2")

#add subitem for item2
tree.insert(item2,"end","subitem2_1",text="subitem2.1")

tree.insert(item2,"end","subitem2_2",text="subitem2.2")

#add subitem for item3
tree.insert(item3,"end","subitem3_1",text="subitem3.1")

tree.insert(item3,"end","subitem3_2",text="subitem3.2")
root.mainloop()


