from tkinter import *
#this is program to implement sub menus
def mycolor(myself):
       window.configure(bg="red")
window=Tk()
window.title("new winodw")
menubar=Menu(window)
menubar.add_command(label="red")
menubar.add_command(label="blue")
menubar.add_command(label="yellow")
menubar.add_command(label="orange")
window.config(menu=menubar)
window.configure(bg="black")
window.mainloop()