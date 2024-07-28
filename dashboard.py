import streamlit as st
import pandas as pd
import plotly.express as px


def display():
    st.markdown("<h1 style='color: red;'>Dashboard</h1>", unsafe_allow_html=True)

    # Load data from the uploaded CSV files
    try:
        df_movies = pd.read_csv(r"E:\MovieRecommendationProject\dataset\tmdb_5000_movies.csv")
        df_credits = pd.read_csv(r"E:\MovieRecommendationProject\dataset\tmdb_5000_credits.csv")
    except FileNotFoundError:
        st.error("File not found. Please ensure the dataset files are in the correct location.")
        return
    except pd.errors.EmptyDataError:
        st.error("The dataset file is empty.")
        return
    except pd.errors.ParserError:
        st.error("Error parsing the dataset file.")
        return

    # Drop or rename columns that will cause duplicates before merging
    df_credits.drop(columns=['title'], inplace=True)  # 'title' already in df_movies

    # Merge the datasets on 'id' column
    df = pd.merge(df_movies, df_credits, left_on='id', right_on='movie_id')

    # Rename columns to avoid confusion
    df.rename(columns={'title_x': 'title', 'title_y': 'original_title'}, inplace=True)

    # Drop rows with missing values in 'vote_average' and 'genres'
    df.dropna(subset=['vote_average', 'genres'], inplace=True)

    # Convert 'genres' from string to list of genres
    df['genres'] = df['genres'].apply(lambda x: [d['name'] for d in eval(x)])

    # Cards displaying key statistics
    total_movies = df.shape[0]
    avg_rating = df['vote_average'].mean()
    total_revenue = df['revenue'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Movies", total_movies)
    col2.metric("Average Rating", f"{avg_rating:.2f}")
    col3.metric("Total Revenue", f"${total_revenue:,.2f}")

    # Movie Ratings Distribution
    fig_ratings_dist = px.histogram(df, x='vote_average', nbins=20, title="Distribution of Movie Ratings", color_discrete_sequence=['blue'])
    fig_ratings_dist.update_layout(width=400, height=400, showlegend=False)

    # Top 10 Genres by Number of Movies
    all_genres = df['genres'].explode()
    top_genres = all_genres.value_counts().head(10)
    fig_top_genres = px.bar(top_genres, x=top_genres.index, y=top_genres.values,
                            title="Top 10 Genres by Number of Movies", color=top_genres.index, color_discrete_map={'Action': 'red', 'Adventure': 'green', 'Comedy': 'blue', 'Drama': 'orange'})
    fig_top_genres.update_layout(width=400, height=400, showlegend=False)

    # Top 10 Movies by Revenue
    top_movies_revenue = df.nlargest(10, 'revenue')
    fig_top_revenue = px.bar(top_movies_revenue, x='title', y='revenue', title="Top 10 Movies by Revenue", color='title', color_discrete_sequence=['purple'])
    fig_top_revenue.update_layout(width=400, height=400, showlegend=False)

    # Average Rating by Genre
    genre_rating = df.explode('genres').groupby('genres')['vote_average'].mean().sort_values(ascending=False).head(10)
    fig_avg_rating_genre = px.bar(genre_rating, x=genre_rating.index, y=genre_rating.values,
                                  title="Average Rating by Genre", color=genre_rating.index, color_discrete_map={'Action': 'red', 'Adventure': 'green', 'Comedy': 'blue', 'Drama': 'orange'})
    fig_avg_rating_genre.update_layout(width=400, height=300, showlegend=False)

    # Movie Count by Release Year (Last 20 Years)
    current_year = 2024  # Assuming the current year is 2024
    df['release_year'] = pd.to_datetime(df['release_date']).dt.year
    recent_years = range(current_year - 20, current_year)
    movie_count_by_year = df[df['release_year'].isin(recent_years)]['release_year'].value_counts().reset_index()
    movie_count_by_year.columns = ['release_year', 'count']
    fig_movie_count_by_year = px.pie(movie_count_by_year, values='count', names='release_year',
                                     title='Movie Count by Release Year (Last 20 Years)', color='release_year')
    fig_movie_count_by_year.update_layout(width=600, height=400, showlegend=False)


    # Top Directors by Number of Movies
    df['crew'] = df['crew'].apply(eval)
    directors = df['crew'].apply(
        lambda x: [crew_member['name'] for crew_member in x if crew_member['job'] == 'Director'])
    all_directors = directors.explode()
    top_directors = all_directors.value_counts().head(20)
    fig_top_directors = px.bar(top_directors, x=top_directors.index, y=top_directors.values,
                               title="Top 20 Directors by Number of Movies", color=top_directors.index, color_discrete_sequence=px.colors.qualitative.Set2)
    fig_top_directors.update_layout(width=400, height=400, showlegend=False)

    # Production Companies with Highest Average Revenue
    df['production_companies'] = df['production_companies'].apply(lambda x: [d['name'] for d in eval(x)])
    avg_revenue_by_company = df.explode('production_companies').groupby('production_companies')[
        'revenue'].mean().sort_values(ascending=False).head(10)
    fig_avg_revenue_by_company = px.bar(avg_revenue_by_company, x=avg_revenue_by_company.index,
                                        y=avg_revenue_by_company.values,
                                        title="Production Companies with Highest Average Revenue", color=avg_revenue_by_company.index, color_discrete_sequence=px.colors.qualitative.Set3)
    fig_avg_revenue_by_company.update_layout(width=600, height=400, showlegend=False)



    # Display figures side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        st.plotly_chart(fig_ratings_dist, use_container_width=True)

    with col2:
        st.plotly_chart(fig_top_genres, use_container_width=True)

    with col3:
        st.plotly_chart(fig_top_revenue, use_container_width=True)




    # Display the rest of the charts below the first row
    st.plotly_chart(fig_avg_revenue_by_company, use_container_width=True)


    col5, col6, col7 = st.columns(3)

    with col5:
        st.plotly_chart(fig_movie_count_by_year, use_container_width=True)

    with col6:
        st.plotly_chart(fig_top_directors, use_container_width=True)

    with col7:
        st.plotly_chart(fig_avg_rating_genre, use_container_width=True)


# Run the display function to render the dashboard




# Run the display function to render the dashboard
if __name__ == "__main__":
    display()
