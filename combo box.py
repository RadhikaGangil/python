import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
window = tk.Tk() 
window.title('Combobox') 
window.geometry('5000x2500') 
  
# label text for title 
ttk.Label(window, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1) 
  
# label 
ttk.Label(window, text = "Select the day :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' sunday',  
                          'monday', 
                          ' tuesday', 
                          ' wednesday', 
                          '  thrusday', 
                          ' friday',
                          'saturday') 
  
monthchoosen.grid(column = 1, row = 5) 
monthchoosen.current() 
window.mainloop() 

import tkinter as tk
from tkinter import ttk

def show_selection(event):
    selected_item = combo.get()  # Get the selected item from the combobox
    label.config(text=f"Selected: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("Combo List Example")

# Create a list of items
items = [' sunday',  
                          'monday', 
                          ' tuesday', 
                          ' wednesday', 
                          '  thrusday', 
                          ' friday',
                          'saturday']

# Create a Combobox
combo = ttk.Combobox(root, values=items)
combo.pack(pady=10)

# Set default value
combo.set('Select an item')

# Bind the selection event
combo.bind("<<ComboboxSelected>>", show_selection)

# Create a label to show the selected item
label = tk.Label(root, text="Selected: ")
label.pack(pady=10)

# Run the main loop
root.mainloop()
