import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
import io

# ----------------------------------------------------
# Page Setup (Dark Netflix Theme)
# ----------------------------------------------------
st.set_page_config(page_title="Netflix Movie Recommendation", layout="wide")

st.markdown("""
    <style>
        body { background-color: #0d0d0d; }
        .title { 
            font-size: 46px; 
            font-weight: 800; 
            color: #E50914; 
            text-align:center; 
            margin-top: -40px;
            text-shadow: 0px 0px 20px rgba(229,9,20,0.6);
        }
        .movie-card img {
            border-radius: 12px;
            transition: transform .3s;
        }
        .movie-card:hover img {
            transform: scale(1.08);
            box-shadow: 0px 0px 25px rgba(229,9,20,0.5);
        }
        .movie-name {
            text-align:center;
            margin-top: 8px;
            font-size: 16px;
            color: white;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🎬 Netflix-Style Movie Recommendation</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# Google Drive Links for Large Files
# ----------------------------------------------------
MOVIES_URL = "https://drive.google.com/uc?export=download&id=1tnA7-HNQK-OwdGwzGfNBenfijDCRv7TA"
SIM_URL = "https://drive.google.com/uc?export=download&id=1UUMf4GRrFpiab4_9peK7GGH21p9MCq5D"

# ----------------------------------------------------
# Load Data with caching
# ----------------------------------------------------
@st.cache_resource
def load_pickle_from_url(url):
    r = requests.get(url)
    r.raise_for_status()
    return pickle.load(io.BytesIO(r.content))

@st.cache_resource
def load_numpy_from_url(url):
    r = requests.get(url)
    r.raise_for_status()
    return np.load(io.BytesIO(r.content))

movies = load_pickle_from_url(MOVIES_URL)
similarity = load_numpy_from_url(SIM_URL)
movie_list = movies["title"].values

TMDB_API_KEY = "e04691e95a5f87647ec04389ffb6b282"

# ----------------------------------------------------
# Fetch Poster with caching
# ----------------------------------------------------
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        data = requests.get(url).json()
        poster = data.get("poster_path")
        if poster:
            return "https://image.tmdb.org/t/p/w500" + poster
        return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# ----------------------------------------------------
# Recommend Movies
# ----------------------------------------------------
def recommend(movie):
    try:
        idx = movies[movies["title"] == movie].index[0]
        distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)
        names, posters = [], []
        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            names.append(movies.iloc[i[0]].title)
            posters.append(fetch_poster(movie_id))
        return names, posters
    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")
        return [], []

# ----------------------------------------------------
# UI
# ----------------------------------------------------
selected_movie = st.selectbox("Search a movie", movie_list)

if st.button("Show Recommendation"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)
    if names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{posters[i]}" width="190">
                        <div class="movie-name">{names[i]}</div>
                    </div>
                """, unsafe_allow_html=True)


