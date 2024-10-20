import json
import os.path
from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Any

from config import PATH
from src.Vacancy import Vacancy


class FileSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: Any) -> None:
        pass

    @abstractmethod
    def get_vacancy_by_word(self, word: Any) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Any) -> None:
        pass


class JSONSaver(FileSaver):

    def __init__(self, filename: str = "vacancies.json") -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.__file_path = os.path.join(PATH, filename)

    def __save_to_file(self, vacancies: list[dict]) -> None:
        """Метод для сохранения данных в json-файл"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "a", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
        else:
            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def __read_file(self) -> list[dict[Any, Any]]:
        """Метод для чтения данных из json-файла"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data: list[dict[Any, Any]] = json.load(f)
        except FileNotFoundError:
            data = []
        except JSONDecodeError:
            data = []

        return data

    def add_vacancy(self, vacancy: Vacancy) -> None:
        """Метод для добавления вакансии в файл"""
        vacancies_list = self.__read_file()

        if vacancy.url not in [vac["url"] for vac in vacancies_list]:
            vacancies_list.append(vacancy.to_dict())
            self.__save_to_file(vacancies_list)

    def add_vacancies(self, vacancies: list[dict]) -> None:
        """Метод для добавления списка вакансий в файл"""
        self.__save_to_file(vacancies)

    def delete_vacancy(self, url: str) -> Any:
        """Метод для удаления вакансии из файла"""
        vacancies_list = self.__read_file()
        for index, vacancy in enumerate(vacancies_list):
            if vacancy["url"] == url:
                vacancies_list.pop(index)

        self.__save_to_file(vacancies_list)

    def get_vacancy_by_word(self, word: str) -> Any:
        """Возвращает список вакансий по ключевому слову в названии вакансии"""
        found_vacancies = []

        for vacancy in self.__read_file():
            vacancy_name = vacancy.get("name")
            if vacancy_name is not None and word.lower() in vacancy_name.lower():
                found_vacancies.append(vacancy)

        return Vacancy.vacancies_list_to_vacancy(found_vacancies)
