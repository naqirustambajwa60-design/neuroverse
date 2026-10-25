from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NeuroVerse — Visual AI", page_icon="🧠", layout="wide")

# Remove Streamlit's default padding, header and footer so the visualization fills the screen
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("neuroverse.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=True)
