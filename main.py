import streamlit as st

st.header("App name", divider = 'violet')
st.subheader("What is this app do")
app_description = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum.
'''

st.markdown(app_description)
text_field_code = '''
st.button("Button")
st.button("Reset", type="primary")
'''
input_value = st.text_input("Input your interested word", placeholder="Toyota formula")
st.write('The current input word is', input_value)

# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #6FC276;
# }
# </style>""", unsafe_allow_html=True)
st.button("Submit",type="primary")
result = '''
It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.
Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy.
Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
'''
st.markdown("#### **Result**")
st.markdown(result)
# input_element = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.'''

# # st.markdown(input_element)


