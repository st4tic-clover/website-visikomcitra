import io
import traceback

import streamlit as st
from PIL import Image, UnidentifiedImageError

import content as C
from components import ui
from services.predictor import predict_image

S = C.SCREENING
ss = st.session_state
ss.setdefault("uploader_key", 0)

ui.page_header(S["title"], S["subtitle"])
steps_slot = st.empty()
holder = st.empty()          # seluruh kartu unggah; dikosongkan saat analisis berjalan
analyze = False
image = None
raw = None

with holder.container(key="card"):
    guide = "".join(f"<li>{g}</li>" for g in S["guide"])
    st.html(f'<div class="rc-guide"><strong>{S["guide_title"]}</strong><ul>{guide}</ul></div>')

    uploaded = st.file_uploader(
        S["uploader_label"],
        type=["jpg", "jpeg", "png"],
        key=f"uploader_{ss.uploader_key}",
        label_visibility="collapsed",
    )

    if uploaded is not None:
        raw = uploaded.getvalue()
        try:
            Image.open(io.BytesIO(raw)).verify()           # validasi isi file
            image = Image.open(io.BytesIO(raw)).convert("RGB")
        except (UnidentifiedImageError, OSError):
            st.error(S["invalid_image"])

    if image is not None:
        with st.container(key="preview"):
            st.image(image, caption=f"{uploaded.name} · {len(raw) / 1024:.0f} KB")
            c1, c2 = st.columns(2)
            if c1.button(S["reset"], use_container_width=True):
                ss.uploader_key += 1
                st.rerun()
            analyze = c2.button(S["analyze"], type="primary", use_container_width=True)

steps_slot.html(ui.steps_html(2 if image is not None else 1, S["step_labels"]))

if analyze:
    holder.empty()
    steps_slot.html(ui.steps_html(3, S["step_labels"]))
    prediction = None
    loading = st.empty()
    with loading.container(key="loadcard"):
        st.html(ui.loading_html(S["loading_title"], S["loading_msgs"]))
        try:
            prediction = predict_image(image)               # <- titik integrasi model
        except Exception:
            traceback.print_exc()                           # detail error tampil di terminal
    loading.empty()

    if prediction is None:
        steps_slot.html(ui.steps_html(2, S["step_labels"]))
        st.error(S["predict_failed"])
        if st.button(S["retry"], type="primary"):
            st.rerun()
        ui.footer(C.FOOTER)
        st.stop()

    ss.result = {"label": prediction.label, "confidence": prediction.confidence}
    ss.image_bytes = raw
    st.switch_page("views/result.py")

ui.footer(C.FOOTER)
