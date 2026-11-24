"""
Entry point. Jalankan dengan:  streamlit run app.py
Tugas file ini: konfigurasi halaman, CSS global, header navigasi, dan routing.
"""
from html import escape
from pathlib import Path

import streamlit as st

import content as C

st.set_page_config(page_title=C.APP_NAME, page_icon="👁️", layout="wide", initial_sidebar_state="collapsed")

css = (Path(__file__).parent / "assets" / "style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

home = st.Page("views/home.py", title="Beranda", default=True)
screening = st.Page("views/screening.py", title="Screening", url_path="screening")
result = st.Page("views/result.py", title="Hasil", url_path="hasil")
pg = st.navigation([home, screening, result], position="hidden")

with st.container(key="topbar"):
    c_brand, c_home, c_scr = st.columns([6, 1.3, 1.3], vertical_alignment="center")
    c_brand.html(f'<div class="rc-brand"><span class="rc-logo">◉</span>{escape(C.APP_NAME)}</div>')
    c_home.page_link(home, label="Beranda")
    c_scr.page_link(screening, label="Screening")

pg.run()
