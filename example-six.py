import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("fish.csv")
    return df

df = load_data()

def main():
    page = st.sidebar.selectbox("select a page", ['home', 'bar chart', 'scatter chart'])
    if page == 'home':
        st.table(df)
    if page == 'bar chart':
        left, right = st.columns(2)
        with left:
            st.bar_chart(df['Width'])
        with right:
            st.bar_chart(df['Height'])
    if page == 'scatter chart':
        st.scatter_chart(df[['Height', 'Width']])

if __name__ == '__main__':
    main()