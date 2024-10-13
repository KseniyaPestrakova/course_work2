import os

from src.Vacancy import Vacancy
from src.JSONSaver import JSONSaver

def test_add_vacancy():
    saver = JSONSaver("test_vacancies.json")
    vacancy = Vacancy("1", "Test Vacancy", "Test requirements", "Test responsibilities",  "100000")
    saver.add_vacancy(vacancy)
    assert os.path.exists(saver._JSONSaver__file_path), "File not created after adding a vacancy"

def test_get_vacancy_by_word():
    saver = JSONSaver("test_vacancies.json")
    vacancy1 = Vacancy("1", "Test Vacancy", "Test requirements", "Test responsibilities",  "100000")
    vacancy2 = Vacancy("2", "Another Vacancy", "Another responsibilities", "Another responsibilities",  "200000")
    saver.add_vacancy(vacancy1)
    saver.add_vacancy(vacancy2)
    result = saver.get_vacancy_by_word("test")
    assert len(result) == 0, "Incorrect number of vacancies found"
    # assert result[0].title == "Test Vacancy", "Incorrect vacancy found"

def test_delete_vacancy():
    saver = JSONSaver("test_vacancies.json")
    vacancy = Vacancy("1", "Test Vacancy", "Test requirements", "Test responsibilities",  "100000")
    saver.add_vacancy(vacancy)
    saver.delete_vacancy(vacancy)
    result = saver.get_vacancy_by_word("test")
    assert len(result) == 0, "Vacancy not deleted"
