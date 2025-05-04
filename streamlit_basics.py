import streamlit as st


# will display text
st.write("Hello world")

#text formatting
st.header("This is Header")
st.subheader("This is Subheader")
st.caption("This is caption")
st.text("This is plain text")




# markdown

st.markdown(""" 
# This is title
## This is header
### subheader -1
#### subheader -2

simple plain text

for *italic* use asterisk
for **bold** format use two asterisk


""")


# success
st.success("this message display text in green background")

  
# warning
st.warning("This message display text in yellow background")

#error
st.error("This message display in red background")