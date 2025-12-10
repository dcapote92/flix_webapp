import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews


def main():
    st.title('Flix App')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Inicio', 'Géneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    match menu_option:
        case 'Inicio':
            st.write('Inicio')
        case 'Géneros':
            show_genres()
        case 'Atores/Atrizes':
            show_actors()
        case 'Filmes':
            show_movies()
        case 'Avaliações':
            show_reviews()


if __name__ == '__main__':
    main()
