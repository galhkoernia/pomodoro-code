import time
import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, timedelta
from plyer import notification
from playsound import playsound
import threading

#Tampilan GUI untuk alarm belajar
class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Belajar")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.alarm_time = tk.StringVar()
        self.status = tk.StringVar(value="Siap untuk belajar!")
        self.remaining = tk.StringVar(value="Set alarm untuk belajar")
        self.is_active = False

        ttk.Label(root, text="Waktu Alarm (HH:MM):").pack(pady=5)
        self.time_entry = ttk.Entry(root, textvariable=self.alarm_time)
        self.time_entry.pack()

        self.countdown_label = ttk.Label(root, textvariable=self.remaining, font=("Arial", 12))
        self.countdown_label.pack(pady=10)

        self.toggle_btn = ttk.Button(root, text="Mulai Alarm", command=self.toggle_alarm)
        self.toggle_btn.pack(pady=10)

        ttk.Label(root, textvariable=self.status, foreground="green").pack()
        self.update_clock()

    def toggle_alarm(self):
        if not self.is_active:
            try:
                jam, menit = map(int, self.alarm_time.get().split(":"))
                now = datetime.now()
                self.target_time = now.replace(hour=jam, minute=menit, second=0)
                if self.target_time <= now:
                    self.target_time += timedelta(days=1)
                self.is_active = True
                self.status.set("Alarm aktif")
                self.toggle_btn.config(text="Matikan Alarm")
            except ValueError:
                self.remaining.set("Format salah! Gunakan HH:MM")
        else:
            self.is_active = False
            self.status.set("Alarm dimatikan.")
            self.remaining.set("Silakan atur ulang.")
            self.toggle_btn.config(text="Mulai Alarm")

    def update_clock(self):
        if self.is_active:
            now = datetime.now()
            selisih = self.target_time - now
            if selisih.total_seconds() <= 0:
                self.remaining.set(" Waktu Belajar Dimulai!")
                self.status.set("Alarm Selesai")
                self.is_active = False
                self.toggle_btn.config(text="Mulai Alarm")

                
                threading.Thread(target=study_and_break_cycle).start()
            else:
                jam, sisa = divmod(int(selisih.total_seconds()), 3600)
                menit, detik = divmod(sisa, 60)
                self.remaining.set(f"{jam:02d}:{menit:02d}:{detik:02d}")
        self.root.after(1000, self.update_clock)


def create_window(message="Halo, waktunya belajar!", position="right"):
    root = tk.Tk()
    root.overrideredirect(True)
    root.configure(bg='lightyellow')
    width, height = 300, 100
    layar_width = root.winfo_screenwidth()
    layar_height = root.winfo_screenheight()

    if position == 'right':
        x = layar_width - width - 10
        y = layar_height - height - 10
    elif position == 'center':
        x = (layar_width - width) // 2
        y = (layar_height - height) // 2
    else:
        x = 100
        y = 100

    root.geometry(f"{width}x{height}+{x}+{y}")
    label = tk.Label(root, text=message, bg='lightyellow', font=('Arial', 12))
    label.pack(expand=True, fill=tk.BOTH)

    def start_drag(event):
        root.x_offset = event.x
        root.y_offset = event.y

    def on_drag(event):
        x = root.winfo_x() - root.x_offset + event.x
        y = root.winfo_y() - root.y_offset + event.y
        root.geometry(f"+{x}+{y}")

    label.bind("<Button-1>", start_drag)
    label.bind("<B1-Motion>", on_drag)

    root.after(5000, root.destroy)
    root.mainloop()


def alarm(duration_minutes, message, alarm_sound='220_Second_Bomb_Timer.mp3'):
    duration = duration_minutes * 60
    notification.notify(
        title='Pengingat',
        message=f"{message} selama {duration_minutes} menit",
        timeout=10
    )
    print(f"[{time.strftime('%H:%M:%S')}] {message} selama {duration_minutes} menit dimulai.")
    try:
        playsound(alarm_sound)
    except Exception as e:
        print(f"Gagal memainkan suara alarm: {e}")
    time.sleep(duration)
    notification.notify(
        title='Waktu Habis',
        message=f"{message} selesai",
        timeout=10
    )

def study_and_break_cycle():
    # Waktu Belajar
    threading.Thread(target=create_window, args=("Waktu belajar dimulai!", "right")).start()
    alarm(45, "Belajar dimulai", "220_Second_Bomb_Timer.mp3")

    # Waktu Istirahat
    threading.Thread(target=create_window, args=("Saatnya istirahat!", "center")).start()
    alarm(15, "Istirahat dimulai", "220_Second_Bomb_Timer.mp3")


if __name__ == "__main__":
    root = tk.Tk()
    app  = AlarmApp(root)
    root.mainloop()