import pandas as pd
import streamlit as st

chickweight = pd.read_csv('chickweight.csv')
columns = st.multiselect(label="Columns to display: ", options=chickweight.columns)
st.line_chart(chickweight[columns])