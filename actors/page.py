import streamlit as st
import pandas as pd
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

    if st.button('Cadastrar'):
        actors.append
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso!')
