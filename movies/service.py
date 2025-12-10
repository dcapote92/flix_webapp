from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def get_movies_titles(self):
        movies = self.get_movies()
        movie_titles = [movies.get('title') for movie in movies]
        return movie_titles

    def create_movie(self, title, genre, release_date, actors, resume):
        movie = dict(
            title=title,
            genre=genre,
            release_date=release_date,
            actors=actors,
            resume=resume
        )
        return self.movie_repository.create_movie(movie)
