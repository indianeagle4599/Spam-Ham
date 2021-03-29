import streamlit as st
import joblib

model = joblib.load('Email_Class')

st.title('Classification as Spam or Ham')
ip = st.text_input('Enter text: ')
  
if len(ip) != 0:
  op = model.predict([ip])
  st.title(op[0])
