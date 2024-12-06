import tkinter as tk

#Creation of the main window. 
root = tk.Tk()
root.title("Basic GUI")
root.geometry("400x300")

#This will allow the user to type into an entry box. 
entry = tk.Entry(root, font=("Times New Roman", 14), width=30)
entry.pack(pady=10)

#The text that the user inputs is saved to be later printed in the window. 
output_text = tk.Label (root, text="", font =("Times New Roman", 20), fg= "green", width=30)
output_text.pack(pady = 10)

#This is what will print the text in the window. 
def print_text():
    entered_text = entry.get()
    output_text.config(text=entered_text)

#This function will end the loop and close the window. 
def end():
    root.quit()

#The submit button will run the print text function. 
submit_button = tk.Button(root, text="Print Text", command=print_text)
submit_button.pack(pady = 20)

#This button will run the end function.  
end_button = tk.Button(root, text = "Exit", command=end)
end_button.pack(pady = 20)

root.mainloop()


