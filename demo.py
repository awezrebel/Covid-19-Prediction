import streamlit as st
import pandas as pd

st.write("""
# My First App
Hello *world!*
""")

df = pd.read_csv("../Data set/covid.csv")
st.line_chart(df.to_records)