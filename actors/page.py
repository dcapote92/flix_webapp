import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actors_service = ActorService()
    actors = actors_service.get_actors()

    if actors:
        st.write('Lista de Atores/Atrizes')
        actors_df = pd.json_normalize(actors)
        AgGrid(
            data=pd.DataFrame(actors_df),
            reload_data=True,
            key='actos_grid',
            show_toolbar=True
        )
    else:
        st.warning('Nenhum Ator/Atriz encontrado.')

    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de nascimento',
        value=datetime.today(),
        min_value=datetime(1900, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA', 'CAN', 'ESP', 'GBR', 'RSA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown
    )

    if st.button('Cadastrar'):
        new_actor = actors_service.create_actor(name, birthday, nationality)
        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao cadastrar Ator/Atriz')
