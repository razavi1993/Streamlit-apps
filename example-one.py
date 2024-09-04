import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(10,3), columns=["A", "B", "C"])
slider_value = st.slider('Select a value', 0, 10)
filtered_df = df[df["A"] < slider_value/10]
st.scatter_chart(filtered_df)