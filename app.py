import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Stramlit Application")
st.subheader("deployment with heroku")
np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,2),columns=['A','B'])
st.dataframe(df)
st.line_chart(df)
