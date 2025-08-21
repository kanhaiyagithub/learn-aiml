import streamlit as st
import pandas as  pd
st.title("Streamlit Text Input")
name = st.text_input('Enter your name')
if name:
    st.write(f'Hello {name}')

age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}')

options = ['Python', 'Java', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language', options)
st.write(choice)
data = {
    "name":["john","jane","Jake","jilli"],
    "Age": [28,24,35,40],
    "city":["New York","Los Angles","Chicago","Houston"]
 }
df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)