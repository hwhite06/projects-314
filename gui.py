import tkinter as tk

# Create a basic window with an entry box and a button
root = tk.Tk()
root.title("Basic Tkinter Test")
root.geometry("400x200")

# Entry widget for text input
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Button that will print the entered text to the console
def print_text():
    print(entry.get())  # Print the entered text when the button is clicked

submit_button = tk.Button(root, text="Print Text", command=print_text)
submit_button.pack(pady=20)

root.mainloop()


