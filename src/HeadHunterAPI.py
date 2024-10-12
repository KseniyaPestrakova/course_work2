from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    '''Абстрактный класс для работы с API сервиса с вакансиями'''

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        pass

class HeadHunterAPI(Parser):
    """Класс для работы с платформой hh.ru"""

    def __init__(self, file_worker):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    @property
    def url(self) -> Any:
        '''Возвращает url'''
        return self.__url

    def load_vacancies(self, keyword):
        '''Получение вакансий по ключевому слову'''
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response:
                vacancies = response.json()['items']
                self.vacancies.extend(vacancies)
                self.params['page'] += 1
            else:
                break

        vacancies_list = []

        if self.__vacancies:

            for vacancy in self.__vacancies:
                name = vacancy.get("name")
                url = vacancy.get("alternate_url")
                requirement = vacancy.get("snippet").get("requirement")
                responsibility = vacancy.get("snippet").get("responsibility")
                salary = ''

                if vacancy.get("salary"):
                    if vacancy.get("salary").get("to"):
                        salary = vacancy.get("salary").get("to")
                    elif vacancy.get("salary").get("from"):
                        salary = vacancy.get("salary").get("from")
                else:
                    salary = 0

                vac = {
                    "name": name,
                    "url": url,
                    "requirement": requirement,
                    "responsibility": responsibility,
                    "salary": salary,
                }
                vacancies_list.append(vac)

        return vacancies_list

    @url.setter
    def url(self, value):
        self._url = value


