"""
Project Name : Password Security Analyzer

Developer : Sanika Patil

Description :
This module performs password security analysis,
calculates password score, entropy,
estimated crack time and suggestions.
"""

import tkinter as tk
from tkinter import messagebox

from analyzer import analyze_password, generate_strong_password
from pdf_export import export_pdf

# Create the main window
window = tk.Tk()

results = None

# Window title
window.title("Password Security Analyzer")

# Window size
window.geometry("700x600")

# Prevent resizing
window.resizable(False, False)

# Track password visibility
password_visible = False

def toggle_password():
    """
    Shows or hides the password in the entry field.
    """
    global password_visible

    if password_visible:
        password_entry.config(show="*")
        show_button.config(text="Show Password")
        password_visible = False
    else:
        password_entry.config(show="")
        show_button.config(text="Hide Password")
        password_visible = True

def analyze():
    """
    Analyze the password entered by the user.
    """

    global results

    password = password_entry.get()

    if password.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a password before analysis."
        )
        return

    results = analyze_password(password)

    score_value.config(text=f"{results['score']}/100")
    strength_value.config(text=results["strength"])
    entropy_value.config(text=f"{results['entropy']} bits")
    crack_value.config(text=results["crack_time"])

    result_text.delete("1.0", tk.END)

    result_text.insert(tk.END, "Suggestions\n")
    result_text.insert(tk.END, "-" * 40 + "\n")

    for suggestion in results["suggestions"]:
        result_text.insert(tk.END, f"• {suggestion}\n")
    
    result_text.insert(tk.END, "-" * 45 + "\n\n")


def generate_password():
    """
    Generates a strong password and displays it in the password field.
    """

    password = generate_strong_password()

    password_entry.delete(0, tk.END)

    password_entry.insert(0, password)

def save_pdf():

    global results

    if results is None:
        messagebox.showwarning(
            "Warning",
            "Please analyze a password before exporting the PDF."
        )
        return

    try:
        export_pdf(results)

        messagebox.showinfo(
            "Success",
            "PDF report saved successfully in reports folder."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

def clear_fields():
    """
    Clears the password field and analysis results.
    """
    global results

    password_entry.delete(0, tk.END)

    result_text.delete("1.0", tk.END)

    score_value.config(text="-")
    strength_value.config(text="-")
    entropy_value.config(text="-")
    crack_value.config(text="-")

    results = {}

    password_entry.focus_set()


# Heading Label
title_label = tk.Label(
    window,
    text="PASSWORD SECURITY ANALYZER",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=20)

# Password Label
password_label = tk.Label(
    window,
    text="Enter Password:",
    font=("Arial", 12)
)

password_label.pack()

# Password Entry
password_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12),
    show="*"
)

password_entry.pack(pady=10)

# Frame to hold buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

# Analyze Button
analyze_button = tk.Button(
    button_frame,
    text="Analyze Password",
    width=18,
    height=2,
    command=analyze
)

analyze_button.grid(row=0, column=0, padx=10)

# Show Password Button
show_button = tk.Button(
    button_frame,
    text="Show Password",
    width=18,
    height=2,
    command=toggle_password
)

show_button.grid(row=0, column=1, padx=10)

generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    width=18,
    height=2,
    command=generate_password
)

generate_button.grid(row=1, column=0, columnspan=2, pady=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=18,
    height=2,
    command=clear_fields
)

clear_button.grid(row=2, column=0, padx=10, pady=10)

exit_button = tk.Button(
    button_frame,
    text="Exit",
    width=18,
    height=2,
    command=window.destroy
)

exit_button.grid(row=2, column=1, padx=10, pady=10)

# Result Frame
result_frame = tk.LabelFrame(
    window,
    text="Analysis Result",
    padx=10,
    pady=10
)

result_frame.pack(fill="x", padx=20, pady=10)

export_button = tk.Button(
    window,
    text="Export PDF",
    width=20,
    command=save_pdf
)

export_button.pack(pady=5)


score_label = tk.Label(result_frame, text="Overall Score :")
score_label.grid(row=0, column=0, sticky="w")

score_value = tk.Label(result_frame, text="-")
score_value.grid(row=0, column=1, sticky="w")


strength_label = tk.Label(result_frame, text="Password Strength :")
strength_label.grid(row=1, column=0, sticky="w")

strength_value = tk.Label(result_frame, text="-")
strength_value.grid(row=1, column=1, sticky="w")


entropy_label = tk.Label(result_frame, text="Password Entropy :")
entropy_label.grid(row=2, column=0, sticky="w")

entropy_value = tk.Label(result_frame, text="-")
entropy_value.grid(row=2, column=1, sticky="w")


crack_label = tk.Label(result_frame, text="Estimated Crack Time :")
crack_label.grid(row=3, column=0, sticky="w")

crack_value = tk.Label(result_frame, text="-")
crack_value.grid(row=3, column=1, sticky="w")

result_text = tk.Text(
    window,
    width=75,
    height=18,
    font=("Consolas", 10)
)

result_text.pack(pady=20)

# Run the application
window.mainloop()

