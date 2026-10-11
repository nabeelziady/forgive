# Website Baikan LDR untuk Buwi — versi Python

Website ini memakai Python + Streamlit. Teksnya bisa kamu ubah di satu file: `app.py`.

## Cara mengedit kata-kata
1. Buka `app.py` dengan VS Code atau Notepad.
2. Di bagian paling atas, cari `EDIT BAGIAN INI SAJA`.
3. Ubah isi variabel seperti `PEMBUKA_SURAT`, `ISI_SURAT`, `PENUTUP_SURAT`, `AJAKAN_BAIKAN`.
4. Untuk kenangan, ubah tanggal, judul, cerita di dalam daftar `KENANGAN`.
5. Simpan file.

Gunakan tanda kutip tiga `""" ... """` untuk teks surat yang lebih dari satu baris. Jangan menghapus tanda kutipnya.

## Cara menjalankan di laptop
1. Pastikan Python terpasang.
2. Ekstrak folder ZIP.
3. Buka Terminal/Command Prompt di folder ini.
4. Jalankan:
   `python -m pip install -r requirements.txt`
5. Lalu:
   `python -m streamlit run app.py`
6. Browser akan membuka website lokal.

## Menambahkan foto
1. Buat folder `images` di dalam folder proyek.
2. Masukkan maksimal tiga foto dan beri nama:
   - `kenangan1.jpg`
   - `kenangan2.jpg`
   - `kenangan3.jpg`
3. Jika nama file berbeda, ubah nilai `foto` di daftar `KENANGAN` pada `app.py`.
4. Pastikan foto masuk ke folder proyek sebelum dipublikasikan.

## Musik
Versi awal ini belum menyertakan musik otomatis. Jika ingin menambah audio, gunakan file musik yang kamu punya hak untuk digunakan. Browser umumnya memblokir autoplay; pengunjung perlu menekan tombol play.

## Cara mempublikasikan secara gratis
Streamlit Community Cloud memerlukan repository GitHub.
1. Buat akun GitHub jika belum punya.
2. Buat repository baru.
3. Unggah `app.py`, `requirements.txt`, dan folder `images` (jika ada foto).
4. Buka https://share.streamlit.io dan masuk dengan GitHub.
5. Klik Create app, pilih repository, branch, dan file `app.py`, lalu Deploy.
6. Setelah selesai, salin URL `*.streamlit.app` dan kirim ke Buwi.

Dokumentasi resmi: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

Catatan: URL publik dapat dibuka orang lain yang memiliki tautannya. Jangan memasukkan informasi pribadi yang tidak ingin dibagikan.
