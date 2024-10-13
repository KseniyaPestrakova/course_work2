import pytest

from src.Vacancy import Vacancy


@pytest.fixture
def one_vacancy():
    vacancy1 = Vacancy('Юрист', 'https://hh', 'требования', 'обязанности', '100000')