#ADMISSION FORM:
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Create the database connection and Faculty table
def create_table():
    conn = sqlite3.connect('college')
    c = conn.cursor()
    try:
        c.execute(''' 
            CREATE TABLE IF NOT EXISTS Faculty (
                Ecode CHAR(5) PRIMARY KEY,
                FacName VARCHAR(40) NOT NULL,
                Subjective VARCHAR(30) NOT NULL,
                experience INTEGER CHECK(experience >= 5)
            )
        ''')
        conn.commit()
    except Exception as e:
        messagebox.showerror("Error", f"Error creating table: {e}")
    finally:
        conn.close()
# Insert a row into the Faculty table
def insert_row():
    conn = sqlite3.connect('college')
    c = conn.cursor()
    try:
        ecode = entry_ecode.get()
        facname = entry_facname.get("1.0", "end-1c").strip()  # Correct way to get data from Text widget
        subject = entry_subject.get("1.0", "end-1c").strip()
        experience = int(entry_experience.get())

        c.execute("INSERT INTO Faculty (Ecode, facName, subject, experience) VALUES (?, ?, ?, ?)",
                  (ecode, facname, subject, experience))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")
        # reset_fields()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Ecode must be unique or experience must be 5 or greater.")
    except Exception as e:
        messagebox.showerror("Error", f"Error inserting data: {e}")
    finally:
        conn.close()
def delete_faculty_by_id():
   
     conn = sqlite3.connect('college')
     c = conn.cursor()
     try:
        # Delete the record with the given ID
        c.execute('DELETE FROM faculty WHERE id = ?', (entry_ecode))
        conn.commit()

        if not entry_ecode:
            print(f"No faculty found with ID {entry_ecode}.")
        else:
            print(f"Faculty with ID {entry_ecode} deleted successfully.")
     except sqlite3.Error as e:
        print(f"Error deleting data: {e}")
     finally:
        conn.close()


# Function to reset the form
def reset_form():
    entry_ecode.delete(0, 'end')  # Clears the full name
    entry_facname.delete("1.0", "end")  # Clears the address
    entry_subject.current(0)  # Resets the course to the first option
    entry_experience.delete(0, 'end')  # Clears the contact number

# Create the main window
root = tk.Tk()
root.title("Student Information Form")
root.geometry("400x450")

# ITM University Gwalior Title
label_title = tk.Label(root, text="ITM University Gwalior", font=("Arial", 16, "bold"), fg="blue")
label_title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Ecode
label_ecode = tk.Label(root, text="Ecode:")
label_ecode.grid(row=1, column=0, padx=10, pady=5)
entry_ecode = tk.Entry(root, width=30)
entry_ecode.grid(row=1, column=1, padx=10, pady=5)

# facname
label_facname = tk.Label(root, text="FacName:")
label_facname.grid(row=2, column=0, padx=10, pady=5)
entry_facname = tk.Text(root, width=30, height=4)  # Multi-line text for FacName
entry_facname.grid(row=2, column=1, padx=10, pady=5)

# subjectname
label_subject = tk.Label(root, text="SubjectName:")
label_subject.grid(row=3, column=0, padx=10, pady=5)  # Moved to row 3
entry_subject = tk.Text(root, width=30, height=4)  # Multi-line text for SubjectName
entry_subject.grid(row=3, column=1, padx=10, pady=5)  # Moved to row 3

# Experience
label_experience = tk.Label(root, text="Experience:")
label_experience.grid(row=4, column=0, padx=10, pady=5)
entry_experience = tk.Entry(root, width=30)
entry_experience.grid(row=4, column=1, padx=10, pady=5)

# Add Button
add_button = tk.Button(root, text="Add", command=insert_row)
add_button.grid(row=5, column=0, padx=10, pady=20)

# delete Button
delete_button = tk.Button(root, text="delete", command=delete_faculty_by_id)
delete_button.grid(row=5, column=1, padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()