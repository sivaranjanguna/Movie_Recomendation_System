import pickle
import streamlit as st
import requests

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies_name, recommended_movies_posters

def fetch_poster(movie_id):
    url =  "https://api.themoviedb.org/3/movie/{}?api_key=e04691e95a5f87647ec04389ffb6b282&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.header("Movies Recommendation System")

movies = pickle.load(open("Model_files/movies_list.pkl", 'rb'))
similarity = pickle.load(open("Model_files/similarity.pkl", 'rb'))

movies_list = movies['title'].values
selected_movies = st.selectbox("Type or select a movie to get similar movies", movies_list)

if st.button("Show Recommendation"):
    recommended_movies_name, recommended_movies_posters = recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies_name[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies_name[1])
        st.image(recommended_movies_posters[1])
    with col3:
        st.text(recommended_movies_name[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies_name[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies_name[4])
        st.image(recommended_movies_posters[4])