import streamlit as st
x = st.slider("X value", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
y = st.slider("Y value", min_value=0.0, max_value=1.0, value=0.5, step=0.05)
st.markdown("Total value: "+str(x+y))
