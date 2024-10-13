import json
import os.path
from abc import ABC, abstractmethod
from json import JSONDecodeError

from config import PATH
from src.Vacancy import Vacancy


class FileSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_word(self, word):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileSaver):

    def __init__(self, filename="vacancies.json"):
        '''Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра.'''
        self.__file_path = os.path.join(PATH, filename)

    def __save_to_file(self, vacancies: list[dict]) -> None:
        '''Метод для сохранения данных в json-файл'''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "a", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)
        else:
            with open(self.__file_path, "w", encoding="utf-8") as f:
                json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def __read_file(self) -> list[dict]:
        '''Метод для чтения данных из json-файла'''
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except JSONDecodeError:
            data = []

        return data

    def add_vacancy(self, vacancy: Vacancy) -> None:
        '''Метод для добавления вакансии в файл'''
        vacancies_list = self.__read_file()

        if vacancy.url not in [vac["url"] for vac in vacancies_list]:
            vacancies_list.append(vacancy.to_dict())
            self.__save_to_file(vacancies_list)

    def add_vacancies(self, vacancies: list[dict]) -> None:
        '''Метод для добавления списка вакансий в файл'''
        self.__save_to_file(vacancies)


    def delete_vacancy(self, url: str) -> None:
        '''Метод для удаления вакансии из файла'''
        vacancies_list = self.__read_file()
        for index, vacancy in enumerate(vacancies_list):
            if vacancy["url"] == url:
                vacancies_list.pop(index)

        self.__save_to_file(vacancies_list)

    def get_vacancy_by_word(self, word: str) -> list[Vacancy]:
        """Возвращает список вакансий по ключевому слову в названии вакансии"""
        found_vacancies = []

        for vacancy in self.__read_file():
            if word in vacancy.get("name").lower():
                found_vacancies.append(vacancy)

        return Vacancy.vacancies_list_to_vacancy(found_vacancies)
