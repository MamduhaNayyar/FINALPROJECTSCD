"""
Hospital Management System
Description: A simple GUI-based application to manage patient records.
Features: Add, View, Search, and Delete patients.
"""

import tkinter as tk
from tkinter import messagebox


# In-memory patient storage (list of dicts)
patients = []


def add_patient():
    """Add a new patient record after validating all input fields."""
    try:
        patient_id = int(entry_id.get())
        name = entry_name.get().strip()
        disease = entry_disease.get().strip()

        if not name or not disease:
            raise ValueError("Name and Disease fields cannot be empty.")

        # Check for duplicate ID
        for p in patients:
            if p["id"] == patient_id:
                messagebox.showerror("Duplicate", f"Patient ID {patient_id} already exists!")
                return

        patients.append({"id": patient_id, "name": name, "disease": disease})
        messagebox.showinfo("Success", f"Patient '{name}' added successfully!")

        # Clear input fields after successful addition
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_disease.delete(0, tk.END)

    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")


def view_patients():
    """Display all patient records in the output text box."""
    text_output.delete("1.0", tk.END)

    if not patients:
        text_output.insert(tk.END, "No patients found.\n")
        return

    text_output.insert(tk.END, f"{'ID':<6} {'Name':<20} {'Disease'}\n")
    text_output.insert(tk.END, "-" * 45 + "\n")

    for p in patients:
        text_output.insert(tk.END, f"{p['id']:<6} {p['name']:<20} {p['disease']}\n")


def search_patient():
    """Search for a patient by their unique ID."""
    try:
        search_id = int(entry_search.get().strip())

        for p in patients:
            if p["id"] == search_id:
                messagebox.showinfo(
                    "Patient Found",
                    f"ID     : {p['id']}\nName   : {p['name']}\nDisease: {p['disease']}"
                )
                return

        messagebox.showerror("Not Found", f"No patient found with ID: {search_id}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric Patient ID.")

 #Added delete patient feature and duplicate ID validation

def delete_patient():
    """Delete a patient record by their unique ID."""
    try:
        del_id = int(entry_search.get().strip())

        for i, p in enumerate(patients):
            if p["id"] == del_id:
                removed = patients.pop(i)
                messagebox.showinfo("Deleted", f"Patient '{removed['name']}' deleted successfully.")
                view_patients()
                return

        messagebox.showerror("Not Found", f"No patient found with ID: {del_id}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric Patient ID.")


# ─── GUI Setup ───────────────────────────────────────────────────────────────

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("450x560")
root.resizable(False, False)

# Title Label
tk.Label(root, text="Hospital Management System", font=("Arial", 14, "bold")).pack(pady=10)

# ── Patient Info Frame ──
frame_input = tk.LabelFrame(root, text="Patient Details", padx=10, pady=10)
frame_input.pack(fill="x", padx=20, pady=5)

tk.Label(frame_input, text="Patient ID:").grid(row=0, column=0, sticky="w")
entry_id = tk.Entry(frame_input, width=30)
entry_id.grid(row=0, column=1, pady=3)

tk.Label(frame_input, text="Name:").grid(row=1, column=0, sticky="w")
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=1, column=1, pady=3)

tk.Label(frame_input, text="Disease:").grid(row=2, column=0, sticky="w")
entry_disease = tk.Entry(frame_input, width=30)
entry_disease.grid(row=2, column=1, pady=3)

tk.Button(frame_input, text="Add Patient", command=add_patient, bg="#4CAF50", fg="white", width=20).grid(
    row=3, column=0, columnspan=2, pady=8
)

# ── Search Frame ──
frame_search = tk.LabelFrame(root, text="Search / Delete Patient", padx=10, pady=10)
frame_search.pack(fill="x", padx=20, pady=5)

tk.Label(frame_search, text="Search by ID:").grid(row=0, column=0, sticky="w")
entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=1, pady=3)

btn_frame = tk.Frame(frame_search)
btn_frame.grid(row=1, column=0, columnspan=2, pady=5)

tk.Button(btn_frame, text="Search", command=search_patient, bg="#2196F3", fg="white", width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete", command=delete_patient, bg="#f44336", fg="white", width=10).pack(side="left", padx=5)

# ── View Frame ──
frame_view = tk.LabelFrame(root, text="All Patients", padx=10, pady=10)
frame_view.pack(fill="both", expand=True, padx=20, pady=5)

tk.Button(frame_view, text="View All Patients", command=view_patients, bg="#9C27B0", fg="white", width=20).pack()

text_output = tk.Text(frame_view, height=10, font=("Courier", 10))
text_output.pack(fill="both", expand=True, pady=5)

root.mainloop()
