import tkinter as tk
from tkinter import messagebox

def submit_report():
    messagebox.showinfo("Report Submitted", "Thank you for submitting the report.")

def show_warning():
    messagebox.showwarning("Warning", "This content violates the community guidelines.")

def show_ban():
    messagebox.showerror("Ban User", "This user has been banned.")

# Create the main application window
root = tk.Tk()
root.title("Moderation App")
root.geometry("300x200")

# Create the UI elements
submit_button = tk.Button(root, text="Submit Report", command=submit_report)
submit_button.pack(pady=10)

warning_button = tk.Button(root, text="Show Warning", command=show_warning)
warning_button.pack(pady=5)

ban_button = tk.Button(root, text="Ban User", command=show_ban)
ban_button.pack(pady=5)

# Start the main event loop
root.mainloop()