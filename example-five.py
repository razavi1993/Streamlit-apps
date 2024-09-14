import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

plt.style.use('bmh')

df = pd.DataFrame({"X": np.random.normal(3,7,50), "Y": np.random.normal(6,4,50), "Z": np.random.normal(-7,3,50)})

fig, ax = plt.subplots(4)

ax[0].scatter(df['X'], df['Y'])
ax[1].scatter(df['X'], df['Y'])
ax[2].hist(df['X'])
ax[3].hist(df['Y'])

st.pyplot(fig)
