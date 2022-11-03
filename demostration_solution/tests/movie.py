import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService

@pytest.fixture()
def movie_dao_fixture():
    """
    fixture for movie service tests
    """
    movie_dao = MovieDAO

    forest = Movie(id=1, title='Sam', year=2019, genre_id=1, director_id=1)

    movie_dao.get_one = MagicMock(return_value=forest)
    movie_dao.get_all = MagicMock(return_value=[forest])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao

class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao_fixture):
        self.movie_service = MovieService(dao=movie_dao_fixture)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id == 1

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert movies is not None
        assert len(movies) == 1

    def test_create(self):
        movies_d = {
            'id': 1,
            'title': 'Sam'
        }

        movie = self.movie_service.create(movies_d)

        assert movie.id is not None

    def test_update(self):
        movies_d = {
            'id': 1,
            'title': 'Sap'
        }

        self.movie_service.update(movies_d)

    def test_partially_update(self):
        movies_d = {
            'id': 1,
            'year': 2020
        }

        movie = self.movie_service.partially_update(movies_d)

        assert movie.year == movies_d.get('year')


    def test_delete(self):
        self.movie_service.delete(1)