from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()

    def get_genres(self):
        return self.genre_repository.get_genres()

    def get_genres_name(self):
        genres = self.get_genres()
        genres_name = [genre.get('name') for genre in genres]
        return genres_name

    def create_genre(self, name: str):
        genre = dict(
            name=name,
        )
        return self.genre_repository.create_genre(genre)
