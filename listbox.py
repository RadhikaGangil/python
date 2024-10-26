import tkinter as tk
root=tk.Tk()
root.title("example of listbox")

#create a list box
listbox =tk.Listbox(root)
listbox.pack()
#adding element in listbox
listbox.insert(1,"item 1")
listbox.insert(2,"item 2")
listbox.insert(3,"item 3")
root.mainloop()
