from tkinter import *
from pyswip import Prolog

# Inisialisasi Prolog dan file basis pengetahuan
prolog = Prolog()
prolog.consult("mental_kids.pl")

# Daftar gejala dan label tampilannya
gejala_list = {
    "sulit_fokus": "Anak sulit fokus",
    "hiperaktif": "Anak sangat hiperaktif",
    "mudah_terdistraksi": "Mudah terdistraksi saat aktivitas",
    "perilaku_berulang": "Melakukan hal yang sama berulang",
    "kesulitan_interaksi": "Kesulitan bersosialisasi",
    "murung": "Tampak murung berkepanjangan",
    "tidak_bersemangat": "Tidak bersemangat dalam aktivitas",
    "menarik_diri": "Menarik diri dari lingkungan",
    "sering_cemas": "Sering terlihat cemas",
    "takut_berlebihan": "Takut secara berlebihan",
    "sulit_tidur": "Kesulitan tidur",
    "perilaku_kompulsif": "Melakukan hal tertentu secara berulang compulsively",
    "pikiran_obsesif": "Sering mengalami pikiran obsesif"
}

# Menyimpan nilai checkbox
gejala_vars = {}

# Fungsi untuk diagnosa
def diagnosa():
    hasil.delete("1.0", END)
    # Clear fakta sebelumnya
    prolog.retractall("gejala(_)")

    # Tambahkan fakta baru berdasarkan gejala yang dipilih
    for gejala, var in gejala_vars.items():
        if var.get() == 1:
            prolog.assertz(f"gejala({gejala})")

    # Cek semua kemungkinan gangguan
    found = False
    for sol in prolog.query("gangguan(X)"):
        hasil.insert(END, f"Diagnosis: Kemungkinan anak mengalami {sol['X'].upper()}\n")
        found = True

    if not found:
        hasil.insert(END, "Tidak ditemukan gangguan berdasarkan gejala yang dipilih.\n")

# GUI Tkinter
root = Tk()
root.title("Sistem Pakar Deteksi Gangguan Mental Anak")
root.geometry("500x600")

Label(root, text="Pilih Gejala yang Dialami Anak:", font=("Arial", 12, "bold")).pack(pady=10)

frame_gejala = Frame(root)
frame_gejala.pack()

# Checkbox untuk tiap gejala
for kode, label in gejala_list.items():
    var = IntVar()
    Checkbutton(frame_gejala, text=label, variable=var, anchor="w", justify="left", wraplength=450).pack(fill="x", padx=10)
    gejala_vars[kode] = var

Button(root, text="Diagnosa", command=diagnosa, bg="blue", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

hasil = Text(root, height=10, width=60, wrap=WORD)
hasil.pack(pady=10)

root.mainloop()
