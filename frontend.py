
import pyecharts as pe
from pyecharts import options as opts
import streamlit as st
import streamlit.components.v1 as components
import time
import numpy as np

# nastavuji položky v menu
streamlit_menu_items = {
    "Get help": "https://google.com",
    'Report a bug': "https://policie.cz",
    'About': "https://streamlit.io",
}
st.set_page_config("Streamlit workshop", layout="wide", initial_sidebar_state="expanded", page_icon="🚗", menu_items=streamlit_menu_items)

# Skryje Streamlit menu a popisky
# st.markdown("""
#     <style>
#     #MainMenu {visibility: hidden;}
#     </style>
# """, unsafe_allow_html=True)
st.markdown("""
    <style>
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Nakreslí graf
[col1, col2] = st.columns(2)
graf = col1.empty()
col2.write("This is a text in the second column")
