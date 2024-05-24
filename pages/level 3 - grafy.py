import streamlit as st
import pyecharts as pe
from pyecharts import options as opts
import time
import numpy as np

st.title("Podstránka s grafy a klíčovými ukazateli")

st.write("Pro načtení dat stiskněte tlačítko :green_circle:")

tlacitko = st.empty()
[col1, col2] = st.columns(2)
graf_vlevo = col1.empty()
graf_vpravo = col2.empty()
if tlacitko.button(":green_circle:"):
    for i in range(10000):
        time.sleep(1)
        c = (
            pe.charts.Bar(opts.InitOpts(width="500px", height="500px",animation_opts=opts.AnimationOpts(False)))
            .add_xaxis(["Microsoft", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
            .add_yaxis('2017-2018 Revenue in (billion $)', np.array([21.2, 20.4, 10.3, 6.08, 4, 2.2]).__mul__(i).tolist())
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Top cloud providers 2018", subtitle="2017-2018 Revenue"),
                toolbox_opts=opts.ToolboxOpts())
            .render_embed() # generate a local HTML file
        )
        with graf_vlevo:
            graf_vlevo.html(c,height=500)
