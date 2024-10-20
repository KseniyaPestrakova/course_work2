from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict, Union

import requests

from src.Vacancy import Vacancy


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword: str) -> Any:
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с платформой hh.ru"""

    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: Dict[str, Union[str, int]] = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list[dict[str, Any]] = []

    def __api_connect(self) -> Optional[requests.Response]:
        """Метод для подключения к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        return response

    def load_vacancies(self, keyword: str) -> List[Vacancy]:
        """Метод для получения вакансий по ключевому слову"""
        self.__params["text"] = keyword
        while int(self.__params.get("page", 0)) < 20:
            response = self.__api_connect()
            if response:
                vacancies = response.json().get("items", [])
                self.__vacancies.extend(vacancies)
                self.__params["page"] = int(self.__params.get("page", 0)) + 1
            else:
                break

        vacancies_list: List[Vacancy] = []

        if self.__vacancies:

            for vacancy in self.__vacancies:
                name = vacancy.get("name", "")
                url = vacancy.get("alternate_url", "")
                requirement = vacancy.get("snippet", {}).get("requirement", "")
                responsibility = vacancy.get("snippet", {}).get("responsibility", "")
                salary = 0

                if vacancy.get("salary"):
                    salary = vacancy["salary"].get("to") or vacancy["salary"].get("from") or 0

                vac = Vacancy(name, url, requirement, responsibility, salary)

                vacancies_list.append(vac)

        return vacancies_list
