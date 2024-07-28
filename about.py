import streamlit as st

def display():
    st.markdown("<h1 style='color: red;'>About</h1>", unsafe_allow_html=True)
    st.write("""
        Welcome to our Movie Recommendation System! This application is designed to help you discover new and exciting movies based on your personal preferences and ratings.

**How it Works**

Our recommendation engine utilizes the power of content-based filtering, an algorithm that analyzes the characteristics and metadata of movies to suggest titles similar to those you have enjoyed in the past. By leveraging information such as genre, plot summary, cast, and user ratings, our system can provide personalized recommendations tailored specifically to your tastes.

**The Dataset**

Our recommendation engine is trained on the comprehensive TMDb (The Movie Database) dataset, which includes a vast collection of movies, TV shows, and their associated metadata. This extensive dataset allows us to analyze and compare various aspects of films, enabling us to make accurate and relevant recommendations.

**User-Friendly Interface**

We understand the importance of an intuitive and user-friendly interface, which is why we have designed our application with a clean and modern layout. Our interface allows you to easily explore movie recommendations, rate films you've watched, and provide feedback to further refine the recommendations over time.

**Developed by Sanu Sharma**

This movie recommendation system was developed by Sanu Sharma as a demonstration of the power and potential of recommendation systems in the entertainment industry. We hope you find our application useful and enjoyable, and we look forward to helping you discover your next favorite movie!
    """)