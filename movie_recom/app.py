import streamlit as st
import time
st.title("Movie Recommender")

movie_title=st.text_input("Input the Mobie name:")
similar="this"
if st.button("Find it!"):
    with st.spinner('Finding similar movies... 🕵️‍♂️'):
        time.sleep(3)
        st.write(f"Let's find similar movies to{movie_title}")
        
st.write(similar)