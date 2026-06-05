import streamlit as st
import pandas as pd
import numpy as np

# Set pahe config
st.set_page_config(
  page_title="Shree's Awesome APP",
  page_icon="🚀",
  layout="wide",                 # "centered" or "wide"
  initial_sidebar_state="expanded"
)

# set the page title
st.title("hello shree you have done the streamlit setup")
st.write("This is a Streamlit app with a custom page title and icon.")
