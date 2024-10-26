from tkinter import * #all modules i need to import
window = Tk()  # Initalize a


label1=Label(window,text="choose your option")
label1.place(x=40,y=20)
label1.pack()
button1=Button(window,text="ok",bg="red",fg="yellow")
button2=Button(window,text="cancel",bg="blue",fg="yellow")
button1.place(x=240,y=60)
button2.place(x=240,y=80)
button1.pack()
button2.pack()
window.title('hello python')
window.geometry("300x200")
window.mainloop()
