POMODORO TIMER DENGAN GUI (Tkinter)  
====================================

Deskripsi:
----------
Pomodoro Timer ini adalah aplikasi manajemen waktu yang dirancang untuk membantu Anda fokus dalam sesi belajar atau bekerja.  
Aplikasi ini menggunakan metode Pomodoro dengan tampilan antarmuka grafis (GUI) menggunakan Tkinter.

Fitur Utama:
------------
✔ Tampilan GUI interaktif  
✔ Timer belajar dan istirahat  
✔ Notifikasi popup menggunakan plyer  
✔ Suara alarm saat sesi berakhir (menggunakan playsound)  
✔ Multithreading agar GUI tetap responsif

Library yang Digunakan:
------------------------
- `time` - Untuk kontrol waktu
- `tkinter` dan `tkinter.ttk` - Untuk tampilan antarmuka pengguna (GUI)
- `datetime`, `timedelta` - Untuk manipulasi waktu
- `plyer.notification` - Untuk menampilkan notifikasi desktop
- `playsound` - Untuk memainkan suara alarm
- `threading` - Agar timer berjalan di background tanpa mengganggu GUI

Cara Menjalankan:
-----------------
1. Pastikan Python 3 sudah terinstall.
2. Install terlebih dahulu library yang dibutuhkan (gunakan pip):
3. Jalankan file Python:


Catatan:
--------
- Suara alarm harus berada dalam satu folder dengan file `.py`, atau sesuaikan path-nya di dalam kode.
- Aplikasi ini cocok digunakan untuk sesi belajar 30 menit dan istirahat 5 menit, atau disesuaikan di dalam kode.

Lisensi:
--------
Proyek ini bersifat open-source dan bebas digunakan untuk pembelajaran.