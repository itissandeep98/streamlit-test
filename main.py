import streamlit as st 
import numpy as np 

st.title("Registration form")

first,last=st.beta_columns(2)
first.text_input("First Name")
last.text_input("Last Name")

email,mob=st.beta_columns([3,1])
email.text_input("email")
mob.text_input("mob")


user,pw,pw2=st.beta_columns(3)
user.text_input("Username")
pw.text_input("Password",type="password")
pw2.text_input("Confirm password",type="password")

ch,b1,sub=st.beta_columns(3)
ch.checkbox("I Agree")
sub.button("Submit")
