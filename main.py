import streamlit as st

st.write('Hello, *World!* :sunglasses:')

st.header("Sheet Cheat", divider = 'violet')
st.subheader("Input Element")


text_field_code = '''
st.button("Button")
st.button("Reset", type="primary")
'''
st.code(text_field_code, language='python')
st.button("Button")
st.button("Reset", type="primary")

# pattern 
# sub-header
# snippet
# element


# input_element = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.'''

# # st.markdown(input_element)