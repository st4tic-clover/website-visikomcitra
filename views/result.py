from html import escape

import streamlit as st

import content as C
from components import ui

R = C.RESULT
ss = st.session_state

if "result" not in ss:
    st.switch_page("views/screening.py")

label = ss.result["label"]
conf = int(round(ss.result["confidence"] * 100))
copy = R[label]
tone = "ok" if label == "no_dr" else "warn"

ui.page_header(R["title"])

with st.container(key="card"):
    col_img, col_txt = st.columns([1, 2], vertical_alignment="center")
    col_img.image(ss.image_bytes)
    col_txt.html(f"""<div class="fade-up d1">
<span class="rc-badge {tone}">{escape(copy['badge'])}</span>
<h2 class="rc-serif rc-restitle">{escape(copy['title'])}</h2>
<div class="rc-small rc-muted">{escape(R['confidence_label'])}</div>
<div class="rc-meter"><i style="width:{conf}%"></i></div>
<div class="rc-small rc-muted">{conf}%</div></div>""")

nxt = "".join(f"<li>{escape(n)}</li>" for n in copy["next"])
st.html(f"""<div class="rc-card rc-gap fade-up d2"><h3 class="rc-serif">{escape(R['explain_title'])}</h3>
<p style="margin:0">{escape(copy['explain'])}</p></div>
<div class="rc-card rc-gap fade-up d3"><h3 class="rc-serif">{escape(R['next_title'])}</h3>
<ul class="rc-next">{nxt}</ul></div>""")

c1, c2 = st.columns(2)
if c1.button(R["again"], type="primary", use_container_width=True):
    for k in ("result", "image_bytes"):
        ss.pop(k, None)
    ss.uploader_key = ss.get("uploader_key", 0) + 1
    st.switch_page("views/screening.py")
if c2.button(R["home"], use_container_width=True):
    st.switch_page("views/home.py")

ui.disclaimer(*C.DISCLAIMER_RESULT, extra_class="rc-gap")
ui.footer(C.FOOTER)
