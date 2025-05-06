import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        dob = dob_entry.get()
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        today = datetime.today()
        age_years = today.year - dob_date.year
        age_months = today.month - dob_date.month
        age_days = today.day - dob_date.day

        if age_days < 0:
            age_months -= 1
            age_days += 30  # Approximation for days in a month
        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(text=f"Your Age: {age_years} Years, {age_months} Months, {age_days} Days")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter the date in DD-MM-YYYY format.")

# Create the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x200")

# Input label and entry
dob_label = tk.Label(root, text="Enter your Date of Birth (DD-MM-YYYY):")
dob_label.pack(pady=10)
dob_entry = tk.Entry(root, width=20)
dob_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
