from tkinter import *
#this is program to implement sub menus
def red():
       window.configure(bg="red")
def blue():
       window.configure(bg="blue")
def yellow():
       window.configure(bg="yellow")
def orange():
       window.configure(bg="orange")
def golden():
       window.configure(bg="golden")
window=Tk()
window.title("new winodw")
menubar=Menu(window)
menubar.add_command(label="red",command=red)
menubar.add_command(label="blue",command=blue)
menubar.add_command(label="yellow",command=yellow)
menubar.add_command(label="orange",command=orange)
menubar.add_command(label="golden",command=golden)
window.config(menu=menubar)
window.configure(bg="black")
window.mainloop()