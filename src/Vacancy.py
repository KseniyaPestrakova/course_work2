from typing import Any, Union, Optional


class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("name", "url", "requirement", "responsibility", "salary")

    def __init__(self, name: str, url: str, requirement: str, responsibility: str,
                 salary: Optional[Union[int, None]] = None) -> None:
        """Инициализатор класса Vacancy"""
        self.name = name
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = self.__salary_validation((salary if salary is not None else 0))

    @staticmethod
    def __salary_validation(salary: Optional[int]) -> int:
        """Валидация зарплаты"""
        if isinstance(salary, (int, float)) and salary >= 0:
            return salary
        return 0

    @classmethod
    def vacancies_list_to_vacancy(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """Возвращает список экземпляров Vacancy из списка словарей"""

        return [cls(**vac) for vac in vacancies]

    def __str__(self) -> str:
        """Метод для строкового представления вакансий"""

        return (
            f"{self.name} (Зарплата: {self.salary if self.salary else 'не указана'}).\n"
            f"Требования: {self.requirement}.\n"
            f"Обязанности: {self.responsibility}.\nСсылка на вакансию: {self.url}"
        )

    @classmethod
    def __check_data(cls, other: Any) -> Any:
        """Метод для проверки типа данных"""
        if not isinstance(other, (float, Vacancy)):
            raise TypeError

        return other if isinstance(other, float) else other.salary

    def __equals__(self, other: Any) -> Any:
        """Метод сравнения вакансий на точное соответствие заданной сумме"""
        sal = self.__check_data(other)
        return self.salary == sal

    def __less__(self, other: Any) -> Any:
        """Метод сравнения вакансий по сумме зарплаты меньше заданной суммы"""
        sal = self.__check_data(other)
        return self.salary < sal

    def __less_equals__(self, other: Any) -> Any:
        """Метод сравнения вакансий по сумме зарплаты, больше или равной заданной сумме"""
        sal = self.__check_data(other)
        return self.salary >= sal

    def to_dict(self) -> Any:
        """Возвращает словарь с данными о вакансии из экземпляра класса Vacancy"""
        return {
            "name": self.name,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "salary": self.salary,
        }
