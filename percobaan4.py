import tkinter as tk
from tkinter import ttk
# Inisialisasi window utama
root = tk.Tk()
root.title("Sistem Pakar Diagnosis Penyakit Malaria")
# Inisialisasi frame utama
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# Membuat widget yang diperlukan
ttk.Label(mainframe, text="Aplikasi Diagnosa Penyakit Malaria",
font=("Arial", 16)).grid(column=0, row=0, columnspan=3)
ttk.Label(mainframe, text="Kolom Pertanyaan:").grid(column=0, row=1)
kotak_pertanyaan = tk.Text(mainframe, height=4, width=40,
state=tk.DISABLED)
kotak_pertanyaan.grid(column=0, row=2, columnspan=3)
no_btn = ttk.Button(mainframe, text="Tidak", state=tk.DISABLED,
command=lambda: jawaban(False))
no_btn.grid(column=1, row=3, sticky=(tk.W, tk.E))
yes_btn = ttk.Button(mainframe, text="Ya", state=tk.DISABLED,
command=lambda: jawaban(True))
yes_btn.grid(column=2, row=3, sticky=(tk.W, tk.E))
start_btn = ttk.Button(mainframe, text="Mulai Diagnosa",
command=mulai_diagnosa)
start_btn.grid(column=1, row=4, columnspan=2, sticky=(tk.W, tk.E))
# Tambah padding ke setiap widget
for widget in mainframe.winfo_children():
widget.grid_configure(padx=5, pady=5)
# Menjalankan GUI
root.mainloop()
