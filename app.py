import streamlit as st
st.title("Streamlit demo")
st.write("""
# Explore different classifier
Which one is the best ?
""")
dataset_name = st.selectbox("Select Dataset", ["Iris", "Breast Cancer"])