import pickle
import streamlit as st
import requests
import gdown
import os

def download_file_if_not_exists(file_name, file_id):
    """Downloads a file from Google Drive if it does not exist locally."""
    if not os.path.exists(file_name):
        print(f"Downloading {file_name} from Google Drive...")
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        gdown.download(url, file_name, quiet=False)

# Get the file IDs from the URLs you provided
similarity_id = "1BeeqZIAa67kn96Ec80ILOYto9mqvn0Xv"
movies_dict_id = "1tSSzMd3McmJDb5ERmRhN2F61TeWKa3_q"
movies_id = "16BH5DEFQyI-V1z8Eu3Nc60lx8qO0YEdu"

# Download all necessary files if they don't exist
download_file_if_not_exists('movies.pkl', movies_id)
download_file_if_not_exists('movies_dict.pkl', movies_dict_id)
download_file_if_not_exists('similarity.pkl', similarity_id)

# Load the data for use
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
# movies_dict.pkl is not used in the code you provided, so it is not loaded here.

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=23174b7105e74171a70d5f92450333a8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommender System')
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
