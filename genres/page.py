import streamlit as st


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

    st.table(genres)

    st.title('Cadastrar novo Género')
    name = st.text_input('Nome do Género')
    if st.button('Cadastrar'):
        st.success(f'Género "{name}" cadastrado com sucesso!')
