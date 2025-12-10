import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Os Mercenarios'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data=pd.DataFrame(movies),
        reload_data=True,
        key='movies_grid',
        show_toolbar=True
    )

    st.title('Cadastrar novo Filme')
    name = st.text_input('Nome do Filme')
    if st.button('Cadastrar'):
        st.success(f'Filme "{name}" cadastrado com sucesso!')
