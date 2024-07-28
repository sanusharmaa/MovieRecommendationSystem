import streamlit as st
import pickle

def display():

    st.markdown("<h1 style='color: red;'>Movie Recommender System</h1>", unsafe_allow_html=True)

    # Function to recommend movies based on the selected movie
    def recommend(movie):
        try:
            index = movies[movies['title'] == movie].index[0]
            distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommended_movie_names = []
            for i in distances[1:6]:
                recommended_movie_names.append(movies.iloc[i[0]].title)
            return recommended_movie_names
        except IndexError:
            st.error("Movie not found in database.")
            return []

    # Load movies and similarity data
    try:
        with open('movie_list.pkl', 'rb') as f:
            movies = pickle.load(f)
        with open('similarity.pkl', 'rb') as f:
            similarity = pickle.load(f)
    except FileNotFoundError as e:
        st.error("File not found: " + str(e))
        return

    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        recommended_movie_names = recommend(selected_movie)
        if recommended_movie_names:
            col1, col2, col3, col4, col5 = st.columns(5)
            for idx, movie_name in enumerate(recommended_movie_names):
                with [col1, col2, col3, col4, col5][idx]:
                    st.image(r"E:\MovieRecommendationProject\film-slate.png", width=80)  # Ensure the image path is correct
                    st.write(movie_name)
        else:
            st.write("No recommendations available for this movie.")
