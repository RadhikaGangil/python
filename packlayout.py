import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
label1=tk.Label(root,text="label 1",bg="red")
label1.pack(fill=tk.BOTH,expand=True) # used for diplay on the window

label2=tk.Label(root,text="label 2",bg="blue")
label2.pack(fill=tk.BOTH,expand=True)


root.mainloop()


#p>>2 grid layout
import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
label3=tk.Label(root,text="label 1",bg="black")
label3.grid(row=3,column=3)

label3=tk.Label(root,text="label 3",bg="red")
label3.grid(row=3,column=3)

label2=tk.Label(root,text="label 2",bg="green")
label2.grid(row=2,column=2)
root.mainloop()