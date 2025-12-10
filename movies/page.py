import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    movies_service = MovieService()
    movies = movies_service.get_movies()

    if movies:
        st.write('Lista de Filmes')
        movies_df = pd.json_normalize(movies)
        AgGrid(
            data=pd.DataFrame(movies_df),
            reload_data=True,
            key='movies_grid',
            show_toolbar=True
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar novo Filme')
    title = st.text_input('Nome do Filme')
    genre_service = GenreService()
    genre_dropdown = genre_service.get_genres_name()
    genre = st.selectbox(
        label='Gênero',
        options=genre_dropdown
    )
    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    actor_service = ActorService()
    actors_dropdown = actor_service.get_actors_name()
    actor = st.selectbox(
        label='Ator/Atriz',
        options=actors_dropdown
    )
    resume = st.text_area

    if st.button('Cadastrar'):

        new_movies = movies_service.create_movie(title, genre, release_date, actor, resume)
        if new_movies:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme.')
