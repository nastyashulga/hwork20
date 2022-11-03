import pytest
from unittest.mock import MagicMock

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService

@pytest.fixture()
def genre_dao_fixture():
    """
    fixture for genre service tests
    """
    genre_dao = GenreDAO

    g1 = Genre(id=2, name='step')
    g2 = Genre(id=3, name='amateur')

    genre_dao.get_one = MagicMock(return_value=g1)
    genre_dao.get_all = MagicMock(return_value=[g1, g2])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao_fixture):
        self.genre_service = GenreService(dao=genre_dao_fixture)

    def test_get_one(self):
        genre = self.genre_service.get_one(2)

        assert genre is not None
        assert genre.id == 2

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) == 2

    def test_create(self):
        genre_g = {
            'id': 1,
            'name': 'step'
        }

        director = self.genre_service.create(genre_g)

        assert director.id is not None

    def test_update(self):
        genre_g = {
            'id': 1,
            'name': 'stef'
        }

        self.genre_service.update(genre_g)

    def test_delete(self):
        self.genre_service.delete(1)