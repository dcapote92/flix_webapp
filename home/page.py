import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():

    movies_service = MovieService()
    movies_stats = movies_service.get_movie_stats()

    st.title('Estatísticas de filmes')

    if len(movies_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movies_stats['movies_by_genre'],
            values='count',
            names='genre__name'
        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movies_stats['total_movies'])

    st.subheader('Totala de Avaliações Cadastradas:')
    st.write(movies_stats['total_reviews'])

    st.subheader('Media Geral de Estrelas nas Avaliações')
    st.write(movies_stats['average_stars'])
