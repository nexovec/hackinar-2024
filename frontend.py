
import pyecharts
import streamlit as st
from streamlit_echarts import st_echarts

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

# sidebar
st.sidebar.title("Navigation")
username = "Your Name" # TODO: authentify
st.sidebar.markdown(f"Logged in as :red[{username}]")

# kreslím graf
st.title("zmena")
options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
}
st_echarts(options=options)