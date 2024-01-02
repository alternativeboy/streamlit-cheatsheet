import streamlit as st

st.write('Hello, *World!* :sunglasses:')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)