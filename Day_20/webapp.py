import streamlit as st

st.title('New Web Application')

textInput = st.text_input('Enter your name:', "Chi George Mofor") 

if(st.button('Submit')): 
    nickname = textInput.title()
    st.write('You entered: '+textInput)
