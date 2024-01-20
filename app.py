import streamlit as st
from st_oauth import st_oauth

st.markdown("## This (and above) is always seen")
id = st_oauth('myoauth', 'Click to log into reddit via OAuth')
st.markdown("## This (and below) is only seen after authentication")
