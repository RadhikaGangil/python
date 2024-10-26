import tkinter as tk
from tkinter import ttk,messagebox
import os
window = tk.Tk()
window.title("ITM, Gwalior - Admission Form")
window.geometry("400x300")
window.configure(bg="black")
def reset_fields():
    full_name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
heading = tk.Label(window, text="ITM Gwalior - Admission Form", font=("Arial", 14, "bold"))
heading.place(x=80, y=10)
label1 = tk.Label(window, text="FULL NAME")
label1.place(x=50, y=50)
full_name_entry = tk.Entry(window)
full_name_entry.place(x=150, y=50, width=150)
label2 = tk.Label(window, text="COURSE")
label2.place(x=50, y=100)
# course_entry = tk.Entry(window)
course_entry=ttk.Combobox(values=["BTech","Mtech"])
course_entry.place(x=150, y=100, width=150)
label3 = tk.Label(window, text="CONTACT NO")
label3.place(x=50, y=150)
contact_entry = tk.Entry(window)
contact_entry.place(x=150, y=150, width=150)

    
def add():
    fv1=open("C:\Infosys Python web Development\\AdmissionFormData.Csv","a")    #if we use open mode as append(a) or write(w) it creates the new file if not exist on to given path
    name=full_name_entry.get()
    course=course_entry.get()
    contact=contact_entry.get()
    
    if not full_name_entry.get() or not course_entry.get() or not contact_entry.get():
         messagebox.showerror("Input required")
    else:
        try:
            if not contact_entry or not len(contact_entry)!=10:
                raise ValueError("Number should be 10 digits")
            else:
                data=str(name)+","+str(course)+","+str(contact)+"\n"
                fv1.write(data)
                fv1.close()
                messagebox.showinfo("Added Successfully")
        except Exception as e:
            messagebox.showerror(e)
        
        
        # add_button.bind("<Button>",add)
        # print("Record added successfully")
    

add_button = tk.Button(window, text="ADD", bg="lightblue", width=10,command=add)
add_button.place(x=100, y=200)
reset_button = tk.Button(window, text="RESET", bg="lightblue", width=10, command=reset_fields)
reset_button.place(x=220, y=200)



window.mainloop()





