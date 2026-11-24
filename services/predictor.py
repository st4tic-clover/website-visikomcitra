"""
LAYANAN PREDIKSI (model PyTorch .pth)
=====================================
Satu-satunya file yang perlu diisi untuk menghubungkan model terlatih.
Tampilan (views/) hanya memanggil predict_image() dan tidak tahu apa-apa soal model.

Kontrak yang harus dipertahankan:
    predict_image(image: PIL.Image.Image) -> Prediction
    Prediction.label      : "dr" atau "no_dr"
    Prediction.confidence : float 0..1

Yang perlu diisi (cari TODO):
    1. MODEL_PATH dan CLASS_NAMES.
    2. load_model(): bangun arsitektur, muat bobot .pth, lalu model.eval().
    3. preprocess(): HARUS identik dengan transformasi saat pelatihan
       (ukuran, normalisasi mean/std, urutan channel).
Selama belum diisi, tombol Analisis menampilkan pesan "Analisis gagal"
dan detail error tercetak di terminal.
"""
from dataclasses import dataclass

import streamlit as st
from PIL import Image

MODEL_PATH = "models/resnet18_dr_model.pth"   # letakkan file .pth di folder models/
CLASS_NAMES = ["no_dr", "dr"]         # TODO: urutan indeks kelas sama dengan saat pelatihan


@dataclass
class Prediction:
    label: str
    confidence: float


@st.cache_resource                    # model dimuat sekali, bukan setiap analisis
def load_model():
    # TODO: contoh alurnya (ResNet-18)
    #   model = torchvision.models.resnet18()
    #   model.fc = torch.nn.Linear(model.fc.in_features, <jumlah kelas sesuai pelatihan>)
    #   model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
    #   model.eval()
    #   return model
    raise NotImplementedError("load_model() belum diisi")


def preprocess(image: Image.Image):
    # TODO: ubah PIL.Image menjadi tensor dengan transformasi yang sama seperti pelatihan
    raise NotImplementedError("preprocess() belum diisi")


def predict_image(image: Image.Image) -> Prediction:
    model = load_model()
    x = preprocess(image)
    # TODO: jalankan model dengan torch.no_grad(); softmax jika keluarannya 2 kelas
    #       (sigmoid + ambang batas jika hanya 1 keluaran), lalu ambil kelas dan probabilitasnya
    #   label = CLASS_NAMES[idx]; confidence = float(prob[idx])
    raise NotImplementedError("predict_image() belum diisi")
