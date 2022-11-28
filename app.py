import streamlit as st
title = "subtract 2 numbers"
st.set_page_config(page_title=title)

st.title('subtract 2 numbers')

x = st.number_input('Enter first number')
y = st.number_input('Enter second number')
z=x-y
st.write(z,"is the result")
