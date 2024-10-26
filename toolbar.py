# import tkinter as tk
# def new_file():
#     print("New file created")

# def open_file():
#     print("File Opened")

# def save_file():
#     print("File Saved")
# #create a root example
# root=tk.Tk()
# root.title("Toolbar Example")
# root.geometry("400X300")

# #cearte aframe for the toolbar
# toolbar=tk.Frame(root,bd=1,relief=tk.RAISED)
# toolbar.pack(side=tk.TOP,fill=tk.X)
# new_button=tk.Button(toolbar,text="New",command=new_file)
# new_button.pack(side=tk.LEFT,padx=2,pady=2)

# open_button=tk.Button(toolbar,text="Open",command=open_file)
# open_button.pack(side=tk.LEFT,padx=2,pady=2)

# save_button=tk.Button(toolbar,text="Save",command=save_file)
# save_button.pack(side=tk.LEFT,padx=2,pady=2)
 
# root.mainloop()




import tkinter as tk

def new_file():
    print("new file created")
    
def open_file():
    print("file opened")
    
def save_file():
    print("file saved")
    
    
root =tk.Tk()
root.title("toolbar Example")
root.geometry("400x300")          
toolbar =tk.Frame(root,bd=1,relief=tk.RAISED)
toolbar.pack(side=tk.TOP,fill=tk.X)

new_button =tk.Button(toolbar,text="New" , command=new_file)
new_button.pack(side=tk.LEFT , padx=3,pady=3)

open_button =tk.Button(toolbar,text="Open" , command=open_file)
open_button.pack(side=tk.LEFT , padx=2,pady=2)

save_button =tk.Button(toolbar,text="Save" , command=save_file)
save_button.pack(side=tk.LEFT , padx=2,pady=2)

root.mainloop() 