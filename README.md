# Pembelajaran Fundamental Python

Selamat datang di repositori pembelajaran Python saya! Repositori ini berisi kumpulan skrip dasar dan mini-aplikasi yang saya kembangkan untuk memahami logika pemrograman Python, mulai dari pemahaman struktur data hingga implementasi penanganan *error*.

## Prasyarat

Sebelum menjalankan skrip yang ada di dalam repositori ini, pastikan sistem komputermu sudah memenuhi persyaratan berikut:
* **Python:** Versi 3.12.0 (atau yang lebih baru).

##  Daftar Skrip & Fitur Utama

Repositori ini terbagi menjadi beberapa program terapan dan skrip latihan dasar:

* **Aplikasi Kalkulator Sederhana (`calc_apps.py`)**
  Aplikasi matematika interaktif di terminal yang mendukung operasi tambah, kurang, kali, dan bagi. Skrip ini sudah dilengkapi dengan *error handling* (`ValueError`, `ZeroDivisionError`) serta fitur pembatasan jumlah percobaan *login*/akses untuk mencegah input yang tidak valid.

* **Aplikasi Ujian/Kuis (`exam_apps.py`)**
  Simulasi kuis interaktif yang membaca bank soal dari file eksternal (`question_data.txt`). Aplikasi ini dirancang untuk mengacak urutan soal, mengevaluasi input jawaban pengguna (A, B, C, D), dan menampilkan kalkulasi persentase skor akhir.

* **Manipulasi File (`file.py`)**
  Skrip yang mendemonstrasikan operasi *Input/Output* dasar di Python, khususnya untuk menulis (*write*) dan membaca (*read*) data nilai siswa ke dalam dokumen `score.txt`.

* **Struktur Dasar Python**
  Kumpulan skrip modular untuk melatih pemahaman sintaks fundamental:
  * **Perulangan:** Implementasi *looping* dengan kondisi `break`, `continue`, dan `for-else`.
  * **Kamus Data (`dictionary.py`):** Pengelolaan dan manipulasi struktur data *key-value*.
  * **Penanganan Pengecualian (`error_handling.py`):** Teknik menjaga stabilitas program menggunakan blok `try-except`.
  * **Fungsi Modular (`function.py`):** Pembuatan *function* dengan parameter untuk menghasilkan kode yang bersih dan *reusable*.

## Cara Menjalankan

Setiap skrip dalam repositori ini berjalan secara independen. Kamu bisa menjalankannya langsung melalui terminal atau *command prompt*. 

1. Buka terminal di sistem operasi kamu.
2. Navigasikan ke direktori tempat repositori ini disimpan.
3. Jalankan skrip menggunakan perintah `python` diikuti dengan nama file.

**Contoh eksekusi Kalkulator Sederhana:**
```bash
python calc_apps.py