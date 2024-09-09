import streamlit as st
import time
from utils import movie_finder,creat_x, find_similar_movies,get_content_based_recommedation


st.title("Movie Recommender")

st.markdown('<p class="big-font">Input the movie name or anything similar to the movie you have in your mind:</p>', unsafe_allow_html=True)

movie_title=st.text_input("")

if st.button("Find it!"):
    #with st.spinner('Finding similar movies... 🕵️‍♂️'):
    st.write(f"Let's find similar movies to: {movie_title}")

similar=get_content_based_recommedation(movie_title)
        
st.write(similar)