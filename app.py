import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict= pickle.load(open('move_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title(" Movie Recommender system")

selected_move_name = st.selectbox(
    "How would you like to be contacted?",
     movies['title'].values)
if st.button("recommend"):
    recomendations = recommend(selected_move_name)
    for i in recomendations:
        st.write(i)

