import pytest

from src.Vacancy import Vacancy

@pytest.fixture
def vacancies():
    vacancies = [
        Vacancy("Python Developer", "url1", "req1", "resp1", 1000),
        Vacancy("Java Developer", "url2", "req2", "resp2", 2000),
        Vacancy("Python Engineer", "url3", "req3", "resp3", 3000),
        Vacancy("Data Scientist", "url4", "req4", "resp4", 4000),
        Vacancy("Frontend Developer", "url5", "req5", "resp5", 5000),
    ]

    return vacancies
