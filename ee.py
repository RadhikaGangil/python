from tkinter import *

#create root window
root=Tk()
root.title("main component example")
#create a frame and add it to th e  root window
frame=Frame(root,bg="lightgrey",bd=2,relief=SUNKEN)
frame.pack(padx=5,pady=10)

#create label and add it to the frame
label=Label(frame,text="this is a label")
label.pack(padx=5,pady=5)

#create a button and add it to the frame
button=Button(frame,text="this is a button")
button.pack(padx=5,pady=5)
#start the msin event loop
root.mainloop()
