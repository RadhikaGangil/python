from tkinter import *
def red():
       root.configure(bg="red")
def green():
       root.configure(bg="green")
def orange():
       root.configure(bg="orange")
root=Tk()
mymenu=Menu(root)
mymenu.add_command(label="color")
mymenu.add_command(label="exit")
root.config(menu=mymenu)
mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="red",command=red)
# m1.add_separator()
# m1.add_separator()
# m1.add_separator()
# m1.add_separator()
m1.add_separator()
m1.add_command(label="green",command=green)
m1.add_separator()
# m1.add_separator()
# m1.add_separator()
# m1.add_separator()
# m1.add_separator()
m1.add_command(label="orange",command=orange)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="color",menu=m1)
mainmenu.add_cascade(label="exit",command=exit)
mainmenu.add_cascade(label="blueee")
root.config(menu=mainmenu)
root.mainloop()
