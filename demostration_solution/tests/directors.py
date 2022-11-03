import pytest
from unittest.mock import MagicMock

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService

@pytest.fixture()
def director_dao_fixture():
    """
     fixture for director service tests
    """
    director_dao = DirectorDAO

    sam = Director(id=1, name='Sam')
    kim = Director(id=2, name='Kim')

    director_dao.get_one = MagicMock(return_value=kim)
    director_dao.get_all = MagicMock(return_value=[sam, kim])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao

class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao_fixture):
        self.director_service = DirectorService(dao=director_dao_fixture)

    def test_get_one(self):
        director = self.director_service.get_one(2)

        assert director is not None
        assert director.id == 2

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert directors is not None
        assert len(directors) == 2

    def test_create(self):
        director_d = {
            'id': 1,
            'name': 'Sam'
        }

        director = self.director_service.create(director_d)

        assert director.id is not None

    def test_update(self):
        director_d = {
            'id': 1,
            'name': 'Lila'
        }

        self.director_service.update(director_d)

    def test_delete(self):
        self.director_service.delete(1)


