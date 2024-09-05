import pandas as pd
import streamlit as st

gold = [24, 13, 35, 13, 15, 17, 36, 47]
gem = [12, 43, 17, 11, 54, 21, 43, 11]
players = ["warrior", "snowman", "joker", "champion",
            "king", "knight", "captain", "giant"]

df = pd.DataFrame({"gold": gold, "gem": gem}, index=players)
st.pyplot(df.plot.barh(stacked=True).figure)