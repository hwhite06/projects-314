import tkinter as tk
from tkinter import messagebox

# Function to display a message when the button is clicked
def on_button_click():
    messagebox.showinfo("Hello", "You clicked the button!")

# Create the main window
root = tk.Tk()
root.title("Simple Python GUI")
root.geometry("300x200")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)

# Place the button on the window
button.pack(pady=20)

# Start the main event loop to run the GUI
root.mainloop()
