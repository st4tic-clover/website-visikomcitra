# ARC: AI Retina Checker

Aplikasi web (Streamlit) untuk screening awal retinopati diabetik dari citra retina fundus.
Tampilan sudah selesai. **Yang tersisa adalah menghubungkan model PyTorch (`.pth`) ke aplikasi.**

---

## 1. Menjalankan aplikasi

Pastikan terminal berada di folder yang berisi `app.py`, lalu:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Browser akan terbuka di `http://localhost:8501`. Hentikan dengan `Ctrl + C`.

Selama model belum terhubung, tombol **Analisis Gambar** akan menampilkan
"Analisis gagal. Silakan coba lagi." Itu normal. Detail error-nya tercetak di terminal.

---

## 2. Tugas: menghubungkan model

Semua pekerjaan ada di **satu file: `services/predictor.py`**.
Halaman tampilan (`views/`) tidak perlu diubah. Cari kata `TODO` di file itu.

### Langkah-langkah

1. **Letakkan file `resnet18_dr_model.pth`** di folder `models/`. `MODEL_PATH` sudah menunjuk ke nama itu;
   tinggal isi `CLASS_NAMES` sesuai urutan kelas saat pelatihan.
2. **Isi `load_model()`**: bangun arsitektur ResNet-18 yang sama dengan saat pelatihan
   (`torchvision.models.resnet18`, dengan lapisan terakhir `fc` diganti sesuai jumlah kelas),
   muat bobot dari `.pth`, lalu panggil `model.eval()`.
3. **Isi `preprocess()`**: ubah `PIL.Image` menjadi tensor dengan transformasi
   yang **identik** dengan saat pelatihan.
4. **Isi `predict_image()`**: jalankan model dengan `torch.no_grad()`, ambil softmax,
   lalu kembalikan kelas dan probabilitas tertingginya.
5. **Tambahkan dependensi** ke `requirements.txt` (hapus tanda `#` pada `torch` dan `torchvision`,
   dan tambahkan paket lain yang dipakai prapemrosesan, misalnya `numpy`).

### Kontrak yang harus dipertahankan

```python
predict_image(image: PIL.Image.Image) -> Prediction

Prediction.label       # "dr" atau "no_dr"  (persis dua string ini)
Prediction.confidence  # float 0..1
```

Selama kontrak ini dipenuhi, halaman hasil akan langsung tampil dengan benar.

### Hal yang sering salah

- **Prapemrosesan berbeda dari saat pelatihan** (ukuran gambar, mean/std normalisasi,
  urutan channel RGB/BGR). Model tetap jalan, tapi akurasi turun tanpa pesan error.
- **Urutan `CLASS_NAMES` tidak sama dengan indeks kelas saat pelatihan.**
  Akibatnya hasil "DR" dan "No DR" tertukar tanpa error. Cek dengan satu gambar yang jawabannya sudah diketahui.
- **Cara menyimpan model.** Jika `.pth` berisi `state_dict`, bangun arsitekturnya dulu lalu `load_state_dict`.
  Jika berisi seluruh objek model, PyTorch versi baru (2.6 ke atas) memuatnya dengan `weights_only=True`
  secara bawaan, sehingga bisa gagal. Sesuaikan cara memuatnya dengan cara menyimpannya.
- **Bentuk keluaran model.** Jika `fc` punya 2 keluaran, pakai softmax lalu ambil indeks tertinggi.
  Jika hanya 1 keluaran, pakai sigmoid dan tentukan ambang batasnya (misalnya 0,5).
  Sesuaikan dengan cara model dilatih.
- **Memuat model di dalam `predict_image()`.** Biarkan pemuatan di `load_model()`
  yang sudah memakai `@st.cache_resource`, supaya model hanya dimuat sekali.
- **Gambar non-retina** (foto biasa, poster, dll.) tetap akan mendapat salah satu dari dua kelas.
  Lihat bagian "Catatan" di bawah.

### Cara menguji

1. Jalankan `streamlit run app.py`, buka halaman **Screening**.
2. Unggah satu gambar yang jawabannya sudah diketahui, untuk masing-masing kelas.
3. Pastikan halaman hasil menampilkan label yang benar dan tidak ada error di terminal.

---

## 3. Struktur folder

| Lokasi | Isi | Perlu diubah? |
|---|---|---|
| `app.py` | Pintu masuk, header, navigasi | Tidak |
| `content.py` | Semua teks tampilan | Hanya jika mengubah teks |
| `assets/style.css` | Font, warna, animasi | Tidak |
| `views/` | Halaman: `home.py`, `screening.py`, `result.py` | Tidak |
| `components/ui.py` | Potongan HTML yang dipakai ulang | Tidak |
| `services/predictor.py` | **Penghubung ke model** | **Ya, di sini** |
| `models/` | Tempat file `.pth` | Letakkan model di sini |

---

## 4. Alur kerja aplikasi (ringkas)

```
Home → Screening (unggah gambar → tekan Analisis) → predict_image() → Result
```

Hasil disimpan sementara di `st.session_state`. Tidak ada database, dan gambar tidak disimpan ke disk.

---

## 5. Catatan

- Sistem ini hanya menilai **temuan pada citra retina**, bukan menentukan apakah seseorang
  menderita diabetes. Jaga agar teks dan laporan tetap konsisten dengan hal ini.
- Aplikasi menerima gambar apa saja. Jika ingin menolak gambar yang jelas bukan fundus,
  tambahkan pengecekan sederhana di `predict_image()` (atau tampilkan peringatan di halaman hasil).
  Putuskan bersama kelompok apakah ini diperlukan.
- Hasil model bukan diagnosis medis. Disclaimer sudah ada di halaman Beranda dan Hasil.
