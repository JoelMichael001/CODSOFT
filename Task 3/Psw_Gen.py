import streamlit as st
import random

def psw_gen(charecters, length):
    return ''.join(random.choice(charecters) for i in range(length))

st.title("Password Generator")

a= st.text_input("Charecters for Password(e.g. , abcdef/123/@%#!)")
user_char = list(a)

length = st.slider("Enter the desired length of the Password:", min_value=1, max_value=100, value=10)

if user_char:
        random_string = psw_gen(user_char, length)
        st.info(random_string)
else:
        st.warning("Please enter a list of characters.")
