# desktop_gui/main.py
import tkinter as tk
import requests

def submit_report():
    payload = {
        "type": type_entry.get(),
        "severity": severity_var.get(),
        "location": location_entry.get(),
        "description": description_text.get("1.0", tk.END).strip()
    }
    response = requests.post("http://localhost:5000/report", json=payload)
    if response.status_code == 201:
        status_label.config(text="Report submitted!", fg="green")
    else:
        status_label.config(text="Submission failed.", fg="red")

root = tk.Tk()
root.title("Monsoon Incident Reporter")

tk.Label(root, text="Incident Type").pack()
type_entry = tk.Entry(root)
type_entry.pack()

tk.Label(root, text="Severity").pack()
severity_var = tk.StringVar(value="Medium")
tk.OptionMenu(root, severity_var, "Low", "Medium", "High").pack()

tk.Label(root, text="Location").pack()
location_entry = tk.Entry(root)
location_entry.pack()

tk.Label(root, text="Description").pack()
description_text = tk.Text(root, height=5, width=40)
description_text.pack()

submit_button = tk.Button(root, text="Submit Report", command=submit_report)
submit_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
