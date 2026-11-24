from html import escape

import streamlit as st

import content as C
from components import ui

H = C.HOME

st.html(f"""<section class="rc-hero">
<span class="rc-pill fade-up">{escape(H['pill'])}</span>
<h1 class="rc-serif fade-up d1">{escape(H['title'])}</h1>
<p class="rc-lead fade-up d2">{escape(H['lead'])}</p>
</section>""")

_, mid, _ = st.columns([1, 1, 1])
with mid:
    if st.button(H["cta"], type="primary", use_container_width=True):
        st.switch_page("views/screening.py")

cards = "".join(
    f'<div class="rc-card fade-up d{i + 2}"><div class="rc-num">{i + 1}</div>'
    f'<h3 class="rc-serif">{escape(t)}</h3><p class="rc-muted">{escape(d)}</p></div>'
    for i, (t, d) in enumerate(H["steps"])
)
st.html(f'<h2 class="rc-serif rc-center rc-sec">{escape(H["how_title"])}</h2><div class="rc-grid3">{cards}</div>')

body = "".join(f"<p>{escape(p)}</p>" for p in H["edu_body"])
symptoms = "".join(f"<li>{escape(s)}</li>" for s in H["symptoms"])
st.html(f"""<h2 class="rc-serif rc-center rc-sec">{escape(H['edu_title'])}</h2>
<div class="rc-card rc-edu fade-up"><div>{body}</div>
<div><h3 class="rc-serif">{escape(H['symptoms_title'])}</h3><ul>{symptoms}</ul></div></div>""")

ui.disclaimer(*C.DISCLAIMER_HOME, extra_class="rc-gap")
ui.footer(C.FOOTER)
