import tkinter as tk
from tkinter import messagebox

patients = []

# Add Patient
def add_patient():
    try:
        id = int(entry_id.get())
        name = entry_name.get()
        disease = entry_disease.get()

        if name == "" or disease == "":
            raise ValueError

        patients.append({"id": id, "name": name, "disease": disease})
        messagebox.showinfo("Success", "Patient Added!")

        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_disease.delete(0, tk.END)

    except:
        messagebox.showerror("Error", "Invalid Input!")

# View Patients
def view_patients():
    text_output.delete("1.0", tk.END)
    for p in patients:
        text_output.insert(tk.END, f"{p['id']} | {p['name']} | {p['disease']}\n")

# Search Patient
def search_patient():
    try:
        search_id = int(entry_search.get())
        for p in patients:
            if p["id"] == search_id:
                messagebox.showinfo("Found", f"{p['name']} - {p['disease']}")
                return
        messagebox.showerror("Error", "Patient Not Found")
    except:
        messagebox.showerror("Error", "Invalid ID")

# GUI Setup
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("400x500")

# Labels & Entries
tk.Label(root, text="Patient ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Disease").pack()
entry_disease = tk.Entry(root)
entry_disease.pack()

# Buttons
tk.Button(root, text="Add Patient", command=add_patient).pack(pady=5)
tk.Button(root, text="View Patients", command=view_patients).pack(pady=5)

# Search
tk.Label(root, text="Search by ID").pack()
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_patient).pack(pady=5)

# Output Box
text_output = tk.Text(root, height=10)
text_output.pack()

root.mainloop()