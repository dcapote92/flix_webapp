import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')
        genres_df = pd.json_normalize(genres)
        AgGrid(
            data=pd.DataFrame(genres_df),
            reload_data=True,
            key='genres_grid',
            show_toolbar=True
        )
    else:
        st.warning('Nenhum gênero')

    st.title('Cadastrar novo Gênero')
    name = st.text_input('Nome do Gênero')

    if st.button('Cadastrar'):
        new_genre = genre_service.create_genre(name)
        if new_genre:
            st.rerun()
        else:
            st.error(f'Erro ao cadastrar o gênero {name}')
