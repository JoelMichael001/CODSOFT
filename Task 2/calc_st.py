import streamlit as st
st.image("calc.png",caption=None, width=50 )
# title - to give the title
st.title('Calculator')
a = st.number_input("Enter Number 1")
b = st.number_input("Enter Number 2 ")

k = st.radio("Enter Your Choice", ["Add", "Sub" ,"Mul", "Div"])

if k == "Add":
    c=a+b
    if st.button("Enter"):
      st.info(c)
elif k == "Sub":
    c=a-b
    if st.button("Enter"):
      st.info(c)
elif k == "Mul":
    c=a*b
    if st.button("Enter"):
      st.info(c)
else:
    c=a/b
    if st.button("Enter"):
      st.info(c)




