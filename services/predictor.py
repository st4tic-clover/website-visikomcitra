"""
LAYANAN PREDIKSI (model PyTorch .pth)
=====================================
Satu-satunya file yang perlu diisi untuk menghubungkan model terlatih.
Tampilan (views/) hanya memanggil predict_image() dan tidak tahu apa-apa soal model.

Kontrak yang harus dipertahankan:
    predict_image(image: PIL.Image.Image) -> Prediction
    Prediction.label      : "dr" atau "no_dr"
    Prediction.confidence : float 0..1
"""
from dataclasses import dataclass

import cv2
import numpy as np
import streamlit as st
import torch
import torch.nn as nn
from PIL import Image
from torchvision import models, transforms

MODEL_PATH = "models/resnet18_dr_model.pth"   # letakkan file .pth di folder models/
CLASS_NAMES = ["dr", "no_dr"]                 # Indeks 0 = "dr", Indeks 1 = "no_dr" (sesuai pelatihan)


@dataclass
class Prediction:
    label: str
    confidence: float


def crop_retina(img: np.ndarray, tol: int = 7) -> np.ndarray:
    """Memotong area hitam secara presisi di 4 sisi (identik dengan Colab)."""
    if img.ndim == 2:
        mask = img > tol
        return img[np.ix_(mask.any(1), mask.any(0))]
    elif img.ndim == 3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        mask = gray_img > tol
        check_any = mask.any(axis=1)
        if not check_any.any():
            return img
        return img[np.ix_(mask.any(1), mask.any(0), [True, True, True])]
    return img


@st.cache_resource                    # model dimuat sekali, bukan setiap analisis
def load_model():
    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)
    model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu", weights_only=True))
    model.eval()
    return model


def preprocess(image: Image.Image):
    # 1. Konversi PIL.Image ke array RGB
    img_rgb = np.array(image.convert("RGB"))

    # 2. Auto-Cropping area hitam
    img_cropped = crop_retina(img_rgb, tol=7)

    # 3. CLAHE pada kanal L (LAB Color Space)
    lab = cv2.cvtColor(img_cropped, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    enhanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2RGB)

    # 4. Resize ke 224x224
    resized_img = cv2.resize(enhanced_img, (224, 224), interpolation=cv2.INTER_AREA)

    # 5. Konversi ke Tensor & Normalisasi ImageNet
    transform_tensor = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    pil_processed = Image.fromarray(resized_img)
    return transform_tensor(pil_processed).unsqueeze(0)


def predict_image(image: Image.Image) -> Prediction:
    model = load_model()
    x = preprocess(image)

    with torch.no_grad():
        outputs = model(x)
        prob = torch.softmax(outputs, dim=1)[0]
        idx = int(torch.argmax(prob).item())

    label = CLASS_NAMES[idx]
    confidence = float(prob[idx])
    return Prediction(label=label, confidence=confidence)