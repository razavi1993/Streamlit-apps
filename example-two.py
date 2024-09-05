import pandas as pd
import streamlit as st

fish = pd.read_csv("fish.csv")
st.dataframe(fish)
