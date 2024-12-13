import tkinter as tk
from genome_sequencer import main


window = tk.Tk()
window.title("Genome Sequencer")
window.geometry("300x200")


def One_Sample():
    one_window = tk.Toplevel()
    one_window.title ("Genome Sequencer- One Sample")
    one_window.geometry("400x400")

    Sample_11_Label = tk.Label(one_window, text="File path for sample:", font=("Arial", 12))
    Sample_11_Label.pack(pady=10)
    Sample_11 = tk.Entry(one_window, font=("Arial", 12), width=100)
    Sample_11.pack(pady=10)

    compute_one = tk.Button

def Two_Sample():
    two_window = tk.Toplevel()
    two_window.title("Genome Sequencer- Two Sample")
    two_window.geometry("400x400")

    Sample_21_Label = tk.Label(two_window, text="File path for sample 1:", font=("Arial", 12))
    Sample_21_Label.pack(pady=10)
    Sample_21 = tk.Entry(two_window, font=("Arial", 12), width=100)
    Sample_21.pack(pady=10)

    Sample_22_Label = tk.Label(two_window, text="File path for sample 2:", font=("Arial", 12))
    Sample_22_Label.pack(pady=10)
    Sample_22 = tk.Entry(two_window, font=("Arial", 12), width=100)
    Sample_22.pack(pady=10)


start = tk.Label (window, text="Please choose number of samples:", font=("Arial", 13), width=30)
start.pack(pady = 10)

one_button = tk.Button(window, text="One sample", command=One_Sample)
one_button.pack(pady=20)

two_button = tk.Button(window, text="Two sample", command=Two_Sample)
two_button.pack(pady=20)

window.mainloop()
