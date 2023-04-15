import streamlit as st


st.set_page_config(layout="wide")
col1,col2=st.columns(2)
with col1:
    st.image("./images/photo.jpeg")
with col2:
    userdata="""Myself LoveLakhwani Currently I am doing my graudation in CSE .
    I like to know how different things work and i have interest in coding and i like to 
     real life problems with the help of coding . I am curious how python is applied in so much 
     different areas. So i started to learn python and here are all of my python projects with 
     their source code."""
    st.info(userdata)