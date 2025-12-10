import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


actors = [
    {
        'id': 1,
        'name': 'Leonardo DiCaprio',
        'birthday': '1978-11-11',
        'nationality': 'USA'
    },
    {
        'id': 2,
        'name': 'Chris Rock',
        'birthday': '1978-11-11',
        'nationality': 'USA'

    },
    {
        'id': 3,
        'name': 'Silvester Stallone',
        'birthday': '1978-11-11',
        'nationality': 'USA'
    },
]


def show_actors():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data=pd.DataFrame(actors),
        reload_data=True,
        key='actos_grid',
        show_toolbar=True
    )

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    if st.button('Cadastrar'):
        actors.append
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso!')
