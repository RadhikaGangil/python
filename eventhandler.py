from tkinter import *
def mouseClick(event):
       Message="mouse is clicked at x="+str(event.x)+ ",y="+str(event.y)
       panellabel.config(text=Message)
window=Tk()
label1=Label(window ,text="click me")
label1.pack()
panellabel=Label(window,text="result panel")
label1.bind("<Button>",mouseClick)
b1=Button(window,text="ok",fg="red",bg="orange")
b2=Button(window,text="cancel",fg="green",bg="orange")
b1.pack()
b2.pack()
b1.bind("<Button>",mouseClick)
b2.bind("<Button>",mouseClick)
panellabel.pack()
window.mainloop()