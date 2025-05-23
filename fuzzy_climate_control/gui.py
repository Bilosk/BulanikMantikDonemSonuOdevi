import tkinter as tk
from tkinter import ttk, messagebox
from fuzzy_logic import get_fuzzy_result
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def run_gui():
    window = tk.Tk()
    window.title("Akıllı Isıtma ve Soğutma Sistemi")
    window.geometry("600x650")
    window.resizable(False, False)

    # Başlık
    tk.Label(window, text="Isıtma / Soğutma Kontrolü", font=("Arial", 18, "bold")).pack(pady=10)

    # Ana çerçeve
    main_frame = tk.Frame(window)
    main_frame.pack(pady=10)

    # Girdi alanları
    def create_input(label, from_, to, default):
        tk.Label(main_frame, text=label).pack()
        scale = tk.Scale(main_frame, from_=from_, to=to, orient=tk.HORIZONTAL, length=400)
        scale.set(default)
        scale.pack(pady=5)
        return scale

    room_temp = create_input("Oda Sıcaklığı (°C)", 10, 35, 22)
    outside_temp = create_input("Dış Sıcaklık (°C)", -10, 40, 15)
    comfort_pref = create_input("Konfor Tercihi (1=Serin, 10=Sıcak)", 1, 10, 5)
    hour = create_input("Saat", 0, 24, 12)
    energy_cost = create_input("Enerji Maliyeti (x0.1 ₺/kWh)", 1, 10, 5)

    # Sonuç metni
    result_label = tk.Label(window, text="", font=("Arial", 12), justify=tk.LEFT)
    result_label.pack(pady=10)

    # Matplotlib grafiği için placeholder
    fig, ax = plt.subplots(figsize=(4, 2))
    bar = ax.bar(["Isıtma", "Soğutma"], [0, 0], color=["red", "blue"])
    ax.set_ylim(0, 100)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

    def calculate():
        try:
            r = room_temp.get()
            o = outside_temp.get()
            c = comfort_pref.get()
            h = hour.get()
            e = energy_cost.get() * 0.1

            heat, cool = get_fuzzy_result(r, o, c, h, e)
            result_text = f"🔥 Isıtma: {heat:.2f} %\n❄️ Soğutma: {cool:.2f} %"
            result_label.config(text=result_text)

            # Grafik güncelle
            bar[0].set_height(heat)
            bar[1].set_height(cool)
            canvas.draw()

        except Exception as ex:
            messagebox.showerror("Hata", f"Hesaplama sırasında hata oluştu:\n{str(ex)}")

    # Buton
    tk.Button(window, text="HESAPLA", font=("Arial", 12, "bold"), bg="lightblue", command=calculate).pack(pady=15)

    window.mainloop()
