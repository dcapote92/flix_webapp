import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


reviews = [
    {
        'id': 1,
        'filme': 'Titanic',
        'estrelas': 5
    },
    {
        'id': 2,
        'filme': 'Os Mercenarios',
        'estrelas': 5
    },
    {
        'id': 3,
        'filme': 'Terror',
        'estrelas': 3
    },
]


def show_reviews():
    st.write('Lista de avaliações')

    AgGrid(
        data=pd.DataFrame(reviews),
        reload_data=True,
        key='reviews_grid',
        show_toolbar=True
    )

    st.title('Cadastrar nova Avaliação')
    movie = st.text_input('Nome do Filme')
    stars = st.text_input('Estrelas ( 1 a 5)')
    if st.button('Cadastrar'):
        st.success(f'Avaliação de {stars} estrelas do filme"{movie}" cadastrada com sucesso!')
