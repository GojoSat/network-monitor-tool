import tkinter as tk
from tkinter import ttk, messagebox
from scanner import PortScanner
from database import Database
import datetime

class NetworkMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor Tool")
        self.root.geometry("700x500")
        self.db = Database()

        self.create_ui()

    def create_ui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text="Host:").grid(row=0, column=0, sticky="w")
        self.host_entry = ttk.Entry(frame, width=30)
        self.host_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Port Range (e.g. 20-80):").grid(row=0, column=2, sticky="w")
        self.port_entry = ttk.Entry(frame, width=15)
        self.port_entry.grid(row=0, column=3, padx=5)

        self.start_btn = ttk.Button(frame, text="Start Scan", command=self.start_scan)
        self.start_btn.grid(row=0, column=4, padx=10)

        columns = ("port", "status", "latency")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=20)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=120, anchor="center")
        self.tree.grid(row=1, column=0, columnspan=5, pady=10)

        self.export_btn = ttk.Button(frame, text="Export Results", command=self.export_results)
        self.export_btn.grid(row=2, column=4, pady=5)

    def start_scan(self):
        host = self.host_entry.get().strip()
        port_range = self.port_entry.get().strip()
        if not host or not port_range:
            messagebox.showwarning("Warning", "Please enter host and port range.")
            return

        try:
            start_port, end_port = map(int, port_range.split("-"))
        except:
            messagebox.showerror("Error", "Invalid port range format.")
            return

        self.tree.delete(*self.tree.get_children())
        scanner = PortScanner(host, start_port, end_port, self.display_result)
        scanner.start()

    def display_result(self, port, status, latency):
        self.tree.insert("", tk.END, values=(port, status, f"{latency:.2f} ms" if latency else "—"))
        self.db.insert_result(self.host_entry.get(), port, status, latency, datetime.datetime.now())

    def export_results(self):
        data = self.db.fetch_all()
        if not data:
            messagebox.showinfo("Info", "No data to export.")
            return
        with open("scan_results.txt", "w") as f:
            for d in data:
                f.write(f"{d}\n")
        messagebox.showinfo("Success", "Results exported to scan_results.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitorApp(root)
    root.mainloop()
