import streamlit as st
import pandas as pd
import numpy as np

st.title("Hi")

df = pd.DataFrame({
    'First Column' : [1,2,3,4],
    'Second Column' : [5,6,7,8]
    })

st.write("Here is the DataFrame")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)