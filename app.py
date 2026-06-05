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

try:
    # Read the CSV file
    df = pd.read_csv("healthy_diet_calorie_intake.csv")

    # Show success message
    st.subheader("✅ Successfully read the dataset!")

    # Display the dataset in an interactive table
    st.dataframe(df)

    # Optional: Show dataset info
    st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
    st.write("**Columns:**", list(df.columns))

except FileNotFoundError:
    st.error("❌ CSV file not found. Please make sure 'healthy_diet_calorie_intake.csv' is in the same folder.")
except Exception as e:
    st.error(f"⚠️ Error reading CSV: {e}")
