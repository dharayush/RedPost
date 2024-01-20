# import requests module 
import requests 
import streamlit as st  
# Making a get request 
response = requests.get('https://api.github.com/') 
  
# print response 
st.write(response) 
  
# print links 
st.write(response.links) 
