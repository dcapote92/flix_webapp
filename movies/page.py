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
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])

        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid',
            show_toolbar=True
        )
    else:
        st.warning('Nenhum filme encontrado.')

    st.title('Cadastrar novo Filme')

    title = st.text_input('Nome do Filme')

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {
        genre['name']: genre['id'] for genre in genres
    }

    selected_genre_name = st.selectbox(
        label='Gênero',
        options=list(genre_names.keys())
    )

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {
        actor['name']: actor['id'] for actor in actors
    }
    selected_actor_names = st.multiselect(
        label='Ator/Atriz',
        options=list(actor_names.keys())
    )
    selected_actors_ids = [actor_names[name] for name in selected_actor_names] 
    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movies = movies_service.create_movie(
            title=title,
            genre=genre_names[selected_genre_name],
            release_date=release_date,
            actors=selected_actors_ids,
            resume=resume
        )
        if new_movies:
            st.rerun()
        else:
            st.error('Erro ao cadastrar filme.')
