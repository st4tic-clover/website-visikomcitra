"""
SEMUA TEKS TAMPILAN ADA DI FILE INI.
Silakan edit kalimat-kalimatnya supaya sesuai gaya bahasa kelompok.
Tidak perlu menyentuh file lain untuk mengganti teks.
"""

APP_NAME = "ARC: AI Retina Checker"
FOOTER = "ARC © JAS Hujan 2026"

# ---------- BERANDA ----------
HOME = {
    "pill": "Screening awal retinopati diabetik",
    "title": "Cek kondisi retina lewat foto fundus",
    "lead": "Unggah foto retina, tunggu beberapa detik, lalu lihat hasil screening awalnya. "
            "Tidak perlu daftar atau mengisi formulir.",
    "cta": "Mulai Screening",
    "how_title": "Langkah-langkah",
    "steps": [
        ("Unggah foto", "Pilih atau seret foto fundus (JPG atau PNG) ke halaman screening."),
        ("Periksa gambar", "Lihat pratinjaunya. Kalau buram atau terpotong, ganti dulu."),
        ("Lihat hasil", "Hasil muncul bersama penjelasan dan saran langkah berikutnya."),
    ],
    "edu_title": "Apa itu Retinopati Diabetik?",
    "edu_body": [
        "Retinopati diabetik adalah kerusakan pembuluh darah kecil di retina, bagian mata yang menangkap cahaya. "
        "Penyebabnya kadar gula darah yang tinggi dalam waktu lama.",
        "Pada tahap awal biasanya tidak ada keluhan, jadi pemeriksaan retina berkala penting "
        "untuk penderita diabetes.",
    ],
    "symptoms_title": "Gejala yang perlu diwaspadai",
    "symptoms": [
        "Penglihatan kabur atau berubah-ubah",
        "Bintik atau bayangan yang melayang",
        "Bagian tertentu penglihatan menggelap",
        "Sulit melihat di tempat remang",
    ],
}

# ---------- SKRINING ----------
SCREENING = {
    "title": "Screening Citra Retina",
    "subtitle": "Unggah satu foto fundus, lalu tekan Analisis.",
    "step_labels": ["Unggah", "Periksa", "Analisis"],
    "guide_title": "Sebelum mengunggah",
    "guide": [
        "Gunakan foto retina fundus, bukan foto wajah atau mata biasa.",
        "Pastikan gambar fokus, cukup terang, dan tidak terpotong.",
        "Format JPG, JPEG, atau PNG. Maksimal 10 MB.",
    ],
    "uploader_label": "Unggah citra retina fundus",
    "invalid_image": "File ini tidak bisa dibaca sebagai gambar. Coba file JPG atau PNG lain.",
    "reset": "Hapus / ganti gambar",
    "analyze": "Analisis Gambar",
    "loading_title": "Sedang menganalisis",
    "loading_msgs": "Memeriksa kualitas gambar, memproses citra, menyusun hasil",
    "predict_failed": "Analisis gagal. Silakan coba lagi.",
    "retry": "Coba lagi",
}

# ---------- HASIL ----------
RESULT = {
    "title": "Hasil Screening",
    "confidence_label": "Tingkat keyakinan model",
    "explain_title": "Artinya apa?",
    "next_title": "Langkah yang disarankan",
    "again": "Ulangi Screening",
    "home": "Kembali ke Beranda",
    "no_dr": {
        "badge": "Tidak terdeteksi",
        "title": "Tidak terdeteksi retinopati diabetik",
        "explain": "Sistem tidak menemukan tanda retinopati diabetik pada gambar ini. "
                   "Bukan jaminan retina sehat, apalagi kalau kualitas gambarnya kurang baik.",
        "next": [
            "Tetap jaga gula darah, tekanan darah, dan pola hidup.",
            "Periksa mata rutin sesuai anjuran dokter.",
            "Kalau muncul penglihatan kabur atau bintik melayang, segera periksa.",
        ],
    },
    "dr": {
        "badge": "Terdeteksi indikasi",
        "title": "Terdeteksi indikasi retinopati diabetik",
        "explain": "Sistem menemukan pola yang mengarah ke kemungkinan retinopati diabetik. "
                   "Ini bukan diagnosis. Hanya dokter mata yang bisa memastikannya.",
        "next": [
            "Buat janji dengan dokter mata sesegera mungkin.",
            "Bawa gambar ini dan catatan kadar gula darah Anda.",
            "Kalau penglihatan menurun mendadak, langsung ke fasilitas kesehatan.",
        ],
    },
}

# ---------- DISCLAIMER ----------
DISCLAIMER_HOME = ("Penting", "Situs ini bukan pengganti diagnosis atau konsultasi dokter. "
                   "Hasilnya hanya menilai temuan pada citra retina, bukan menentukan apakah seseorang menderita diabetes.")
DISCLAIMER_RESULT = ("Keterbatasan", "Hasil ini dibuat oleh sistem kecerdasan buatan dan bukan diagnosis medis. "
                     "Kualitas gambar bisa memengaruhi hasil. Konsultasikan selalu dengan dokter mata atau tenaga kesehatan.")
