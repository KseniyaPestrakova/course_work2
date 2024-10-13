import unittest
from unittest.mock import patch, Mock
import requests
from src.HeadHunterAPI import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch('requests.get')
    def test_load_vacancies_success(self, mock_get):
        """Тест на успешное получение вакансий."""

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {
                    'name': 'Sample Job',
                    'alternate_url': 'https://hh.ru/vacancy/1',
                    'snippet': {
                        'requirement': 'Experience required',
                        'responsibility': 'Doing something'
                    },
                    'salary': {'to': 100000}
                }
            ]
        }
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.load_vacancies('python')
        expected_result = [
            {
                'name': 'Sample Job',
                'url': 'https://hh.ru/vacancy/1',
                'requirement': 'Experience required',
                'responsibility': 'Doing something',
                'salary': 100000
            }
        ]
        self.assertEqual(result, expected_result)

    @patch('requests.get')
    def test_load_vacancies_empty_result(self, mock_get):
        '''Тест на пустой результат от API.'''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'items': []}
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.load_vacancies('python')

        self.assertEqual(result, [])

    @patch('requests.get')
    def test_load_vacancies_no_salary(self, mock_get):
        '''Тест на вакансию без указания зарплаты.'''
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'items': [
                {
                    'name': 'Sample Job',
                    'alternate_url': 'https://hh.ru/vacancy/1',
                    'snippet': {
                        'requirement': 'Experience required',
                        'responsibility': 'Doing something'
                    },
                    'salary': None
                }
            ]
        }
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.load_vacancies('python')

        expected_result = [
            {
                'name': 'Sample Job',
                'url': 'https://hh.ru/vacancy/1',
                'requirement': 'Experience required',
                'responsibility': 'Doing something',
                'salary': 0
            }
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()