import tkinter as tk
from tkinter import ttk
import requests

def fetch_reports():
    try:
        response = requests.get("http://localhost:5000/reports")
        response.raise_for_status()  # Raises exception for 4XX/5XX errors
        return response.json()
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error fetching reports: {e}")
        return []  # Return empty list on failure

def build_gui():
    root = tk.Tk()
    root.title("View All Reports")

    # Treeview for table
    columns = ("ID", "Type", "Severity", "Location","Description","Timestamp")
    tree = ttk.Treeview(root, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    reports = fetch_reports()
    for report in reports:
        tree.insert("", tk.END, values=(
            report.get("report_id"),
            report.get("type"),
            report.get("severity"),
            report.get("location"),
	    report.get("description"),
            report.get("timestamp")[:19]  # trim to date+time
        ))

    tree.pack(expand=True, fill="both")

    def refresh_reports():
        # Clear existing data
        for item in tree.get_children():
            tree.delete(item)
        
        # Fetch and insert new data
        reports = fetch_reports()
        for report in reports:
            tree.insert("", tk.END, values=(
                report.get("report_id"),
                report.get("type"),
           	report.get("severity"),
            	report.get("location"),
           	report.get("description"),
            	report.get("timestamp")[:19]  # trim to date+time
            ))
        
        # Schedule next refresh (every 5 seconds)
        root.after(5000, refresh_reports)
    
    refresh_reports()  # Initial load


    root.mainloop()

if __name__ == "__main__":
    build_gui()
