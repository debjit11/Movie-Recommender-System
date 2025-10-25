import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")



def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data["poster_path"]


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    
    return recommended_movies, recommended_posters

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_titles = movies['title'].values


st.set_page_config(page_title="Movie Recommender 🎥", page_icon="🎬", layout="wide")


st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .main-title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        color: #FF4B4B;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #CCCCCC;
        margin-bottom: 40px;
    }
    .movie-title {
        font-size: 16px;
        font-weight: 600;
        color: #F1F1F1;
        text-align: center;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown('<div class="main-title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Find the perfect movie similar to your favorite one 🍿</div>', unsafe_allow_html=True)


select_movie_name = st.selectbox("🎥 Choose a movie you like:", movie_titles)


if st.button("🔥 Show Recommendations"):
    names, posters = recommend(select_movie_name)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.markdown(f'<div class="movie-title">{names[idx]}</div>', unsafe_allow_html=True)

st.markdown("<br><hr><center>Made with ❤️ by Debjit Das</center>", unsafe_allow_html=True)


