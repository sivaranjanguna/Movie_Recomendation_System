import streamlit as st
import requests
import pickle
import os
import gdown

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
# Google Drive IDs for Pickles
# ----------------------------------------------------
FILES = {
    "movies": "1tnA7-HNQK-OwdGwzGfNBenfijDCRv7TA",
    "similarity": "1UUMf4GRrFpiab4_9peK7GGH21p9MCq5D"
}

# ----------------------------------------------------
# Load Pickles (cached locally)
# ----------------------------------------------------
def load_pickle(file_name, file_id):
    if not os.path.exists(file_name):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, file_name, quiet=False)
    with open(file_name, "rb") as f:
        return pickle.load(f)

movies = load_pickle("movies.pkl", FILES["movies"])
similarity = load_pickle("similarity.pkl", FILES["similarity"])
movie_list = movies["title"].values

# ----------------------------------------------------
# TMDB API Key
# ----------------------------------------------------
TMDB_API_KEY = "e04691e95a5f87647ec04389ffb6b282"

# ----------------------------------------------------
# Fetch Poster (cached)
# ----------------------------------------------------
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
        data = requests.get(url).json()
        poster = data.get("poster_path")
        if poster:
            return "https://image.tmdb.org/t/p/w500" + poster
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# ----------------------------------------------------
# Recommend Movies (cached)
# ----------------------------------------------------
@st.cache_data(show_spinner=False)
def recommend(movie):
    idx = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[idx])),
        key=lambda x: x[1],
        reverse=True
    )

    names, posters = [], []
    for i in distances[1:6]:  # top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters

# ----------------------------------------------------
# Streamlit UI
# ----------------------------------------------------
selected_movie = st.selectbox("Search a movie", movie_list)

if st.button("Show Recommendation"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)
        cols = st.columns(5)

        for i, col in enumerate(cols):
            with col:
                st.markdown(
                    f"""
                    <div class="movie-card">
                        <img src="{posters[i]}" width="190">
                        <div class="movie-name">{names[i]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
