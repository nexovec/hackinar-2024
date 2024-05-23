
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
graf = st.empty()
for i in range(10000):
    time.sleep(1)
    c = (
        pe.charts.Bar(opts.InitOpts(animation_opts=opts.AnimationOpts(False)))
        .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis('2017-2018 Revenue in (billion $)', np.array([21.2, 20.4, 10.3, 6.08, 4, 2.2]).__mul__(i).tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Top cloud providers 2018", subtitle="2017-2018 Revenue"),
            toolbox_opts=opts.ToolboxOpts())
        .render_embed() # generate a local HTML file
    )
    with graf:
        components.html(c, width=1000, height=1000)
