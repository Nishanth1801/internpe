import streamlit as st

st.set_page_config(page_title="Verify Internship | Internpe", layout="wide")

with open("verify.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=800, scrolling=True)
