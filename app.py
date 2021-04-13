import streamlit as st
import random

st.title('Temperature Generator')

if st.button("Generate", key=None, help=None):
    st.write(round(random.uniform(35.5,37.5), 1))