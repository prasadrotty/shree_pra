import streamlit as st
import pandas as pd
import numpy as np
import os

col1,col2=st.columns([1,2])
with col2:
   st.image("shrishail's_sister.jpeg",width=700)

with col1:
   st.image("Prasadi.jpeg",width=1700)

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
    st.subheader("Dataset preview")
    st.dataframe(df)
    st.write("Displaying the Dataset",df.shape)
    st.write("Displaying the Features :", df.columns)
  except Exception as e:
        st.error(f"Error reading file: {e}")
else:
  st.info("Plese upload the file")

st.write("Checking the null values", df.isnull().sum())

def data_ana(data):
  st.write("🫣 Here we are seeing Persons age is graterthen 20:", df[df["Age"] >30])
  return

age_dat=data_ana(df)  
age_dat

