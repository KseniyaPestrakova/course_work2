from src.HeadHunterAPI import HeadHunterAPI
from src.Vacancy import Vacancy
from unittest.mock import patch, Mock
import requests


@patch('requests.get')
def test_load_vacancies_returns_list(mock_get):

    mock_response = Mock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [
        {"name": "Vacancy 1", "alternate_url": "url1", "snippet": {"requirement": "", "responsibility": ""},
         "salary": {"to": 1000}},
        {"name": "Vacancy 2", "alternate_url": "url2", "snippet": {"requirement": "", "responsibility": ""},
         "salary": {"from": 500}}
    ]}

    mock_get.return_value = mock_response

    keyword = "Python"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)

    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(vac, Vacancy) for vac in result)


@patch('requests.get')
def test_load_vacancies_with_no_vacancies(mock_get):

    mock_response = Mock(spec=requests.Response)
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": []}

    mock_get.return_value = mock_response

    keyword = "This keyword does not exist"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)

    assert isinstance(result, list)
    assert len(result) == 0
