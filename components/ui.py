"""Potongan HTML kecil yang dipakai ulang di beberapa halaman."""
from html import escape
import streamlit as st


def page_header(title: str, subtitle: str = ""):
    sub = f'<p class="rc-muted">{escape(subtitle)}</p>' if subtitle else ""
    st.html(f'<div class="rc-pagehead fade-up"><h1 class="rc-serif">{escape(title)}</h1>{sub}</div>')


def steps_html(current: int, labels: list[str]) -> str:
    items = []
    for i, label in enumerate(labels, start=1):
        cls = "active" if i == current else ("done" if i < current else "")
        mark = "✓" if i < current else str(i)
        items.append(f'<li class="{cls}"><span>{mark}</span>{escape(label)}</li>')
    return f'<ol class="rc-steps fade-up d1">{"".join(items)}</ol>'


def disclaimer(label: str, text: str, extra_class: str = ""):
    st.html(f'<div class="rc-disclaimer fade-up {extra_class}"><strong>{escape(label)}:</strong> {escape(text)}</div>')


def loading_html(title: str, msgs: str) -> str:
    return (f'<div class="rc-loading"><div class="rc-spin"></div>'
            f'<h2 class="rc-serif">{escape(title)}</h2><p class="rc-muted">{escape(msgs)}</p></div>')


def footer(text: str):
    st.html(f'<div class="rc-footer">{escape(text)}</div>')
