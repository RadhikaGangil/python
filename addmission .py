import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    # Get values from the form
    name = entry_name.get()
    age = entry_age.get()
    gender = combo_gender.get()
    course = combo_course.get()
    
    # Check if all fields are filled
    if not name or not age or not gender or not course:
        messagebox.showwarning("Input Error", "Please fill all fields!")
    else:
        # Display the collected data in a message box
        messagebox.showinfo("Admission Form", f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}")

# Create the main window
root = tk.Tk()
root.title("Admission Form")
root.geometry("300x300")

# Create and place the form fields
tk.Label(root, text=" collegeName:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="FullName:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

# Combo Box for Gender
tk.Label(root, text="Gender:").pack(pady=5)
combo_gender = ttk.Combobox(root, values=["Male", "Female", "Other"])
combo_gender.set("Select Gender")
combo_gender.pack(pady=5)

# Combo Box for Course Selection
tk.Label(root, text="Course:").pack(pady=5)
combo_course = ttk.Combobox(root, values=["B.Sc", "B.Com", "B.Tech", "B.A"])
combo_course.set("Select Course")
combo_course.pack(pady=5)

# Submit Button
submit_btn = tk.Button(root, text="set", command=submit_form)
submit_btn.pack(pady=20)
submit_btn = tk.Button(root, text="Reset", command=submit_form)
submit_btn.pack(pady=20)

# Run the main loop
root.mainloop()




import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def submit_form():
    # Fetching the values from the form fields
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_combo.get()
    course = course_combo.get()
    
    # Simple validation
    if name == "" or age == "" or gender == "" or course == "":
        messagebox.showerror("Input Error", "All fields are required!")
    else:
        # Display the entered data in a message box
        info = f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}"
        messagebox.showinfo("Form Submitted", info)

# Create the main window
root = tk.Tk()
root.title("Admission Form")

# Set window size
root.geometry("300x300")

# Name Label and Entry
name_label = tk.Label(root, text="Name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Age Label and Entry
age_label = tk.Label(root, text="Age:")
age_label.pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

# Gender Label and Combobox
gender_label = tk.Label(root, text="Gender:")
gender_label.pack(pady=5)
gender_combo = ttk.Combobox(root, values=["Male", "Female", "Other"])
gender_combo.pack(pady=5)
gender_combo.set("Select Gender")  # Default text

# Course Label and Combobox
course_label = tk.Label(root, text="Course:")
course_label.pack(pady=5)
course_combo = ttk.Combobox(root, values=["Computer Science", "Mathematics", "Physics", "English"])
course_combo.pack(pady=5)
course_combo.set("Select Course")  # Default text

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# Run the application
root.mainloop()




#p>>>>2 another method
import tkinter as tk
from tkinter import ttk

# Function to get data from the form
def submit_form():
    full_name = entry_name.get()
    address = entry_address.get()  # For multi-line text
    course = combo_course.get()
    contact_no = entry_contact.get()

    print(f"Full Name: {full_name}")
    print(f"Address: {address}")
    print(f"Course: {course}")
    print(f"Contact No: {contact_no}")

# Function to reset the form
def reset_form():
    entry_name.delete(0, 'end')  # Clears the full name
    entry_address.delete("1.0", "end")  # Clears the address
    combo_course.current(0)  # Resets the course to the first option
    entry_contact.delete(0, 'end')  # Clears the contact number

# Create the main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x450")

# ITM University Gwalior Title
label_title = tk.Label(root, text="ITM University Gwalior", font=("Arial", 16, "bold"), fg="blue")
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Full Name
label_name = tk.Label(root, text="Full Name:")
label_name.grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=0, padx=10, pady=5)

# Address
label_address = tk.Label(root, text="Address:")
label_address.grid(row=2, column=0, padx=10, pady=5)
entry_address = tk.Text(root, width=30, height=4)  # Multi-line text for address
entry_address.grid(row=2, column=1, padx=10, pady=5)

# Course (with ComboBox)
label_course = tk.Label(root, text="Course:")
label_course.grid(row=3, column=0, padx=10, pady=5)

# Creating ComboBox for Course selection
course_options = ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Business Administration"]
combo_course = ttk.Combobox(root, values=course_options, width=28)
combo_course.grid(row=3, column=1, padx=10, pady=5)
combo_course.current(0)  # Set default value to the first option

# Set background color of the course combo box to blue
combo_course.configure(background="blue", foreground="white")

# Contact No
label_contact = tk.Label(root, text="Contact No:")
label_contact.grid(row=4, column=0, padx=10, pady=5)
entry_contact = tk.Entry(root, width=30)
entry_contact.grid(row=4, column=1, padx=10, pady=5)

# Add Button
add_button = tk.Button(root, text="Add", command=submit_form)
add_button.grid(row=5, column=0, padx=10, pady=20)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_form)
reset_button.grid(row=5, column=1, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()

