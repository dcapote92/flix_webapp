import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terror'
    },
]


def show_genres():
    st.write('Lista de Géneros')

    AgGrid(
        data=pd.DataFrame(genres),
        reload_data=True,
        key='genres_grid',
        show_toolbar=True
    )

    st.title('Cadastrar novo Género')
    name = st.text_input('Nome do Género')
    if st.button('Cadastrar'):
        st.success(f'Género "{name}" cadastrado com sucesso!')
