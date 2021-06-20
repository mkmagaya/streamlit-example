from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

html_render_title = """
    <style="color:black;text-align:center;>KBS Assignment 2</style>
    """ 
html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:left;">Keras & OpenCV Project</h1>
	</div>
	"""
html_side_temp = """
	<div style ="padding:13px">
	<h1 style ="color:black;text-align:center;">Project Engineers</h1>
    <h3 style ="color:black;text-align:center;">Magaya Makomborero r181571b</h3>
    <h3 style ="color:black;text-align:center;">Mabhuka Oswell r181573f</h3>
	</div>
	"""    
st.title("KBS Assignment 2")
st.markdown(html_temp, unsafe_allow_html = True)
# students = st.markdown(html_side_temp, unsafe_allow_html = True)
st.sidebar.markdown(html_side_temp, unsafe_allow_html = True)

title_container = st.beta_container()
col1, col2 = st.beta_columns([1, 20])
image = Image.open(st.file_uploader("Upload a Video:", type=["mp4"]))
with title_container:
    with col1:
        st.image(image, width=64)
    with col2:
        st.markdown('<h1 style="color: purple;">Suzieq</h1>',
            unsafe_allow_html=True)

imagesLocation = "./kbsLogFiles/frames/*.jpg"
images = glob.glob(imagesLocation)
