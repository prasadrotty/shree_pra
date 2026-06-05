import streamlit as st
import pandas as pd
import numpy as np
import os

# Set pahe config
st.set_page_config(
  page_title="Shree's Awesome APP",
  page_icon="🚀",
  layout="wide",                 # "centered" or "wide"
  initial_sidebar_state="expanded"
)
file_path="healthy_diet_calorie_intake.csv"

if os.path.exists(file_path):
  
  try:
    df=pd.read_csv("healthy_diet_calorie_intake.csv")
    st.sub_headder("Dataset preview")
    st.dataframe(df)
    st.write("Displaying the Dataset",df.shape)
    st.write("Displaying the Features :", df.columns)
  except Exception as e:
        st.error(f"Error reading file: {e}")
else:
  st.info("Plese upload the file")
  


