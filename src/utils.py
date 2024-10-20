from src.Vacancy import Vacancy


def get_vacancies_by_salary(vacancies: list[Vacancy], salary_from: int, salary_to: int) -> list[Vacancy]:
    '''Функция для вывода вакансий по заданному диапазону зарплат'''

    vacancy_from = [vacancy for vacancy in vacancies if vacancy.salary >= salary_from]
    return [vacancy for vacancy in vacancy_from if vacancy.salary <= salary_to]


def filter_vacancies(vacancies: list[Vacancy], filter_word: str) -> list[Vacancy]:
    '''Функция для фильтрации вакансий по заданному слову'''

    return [vacancy for vacancy in vacancies if filter_word in vacancy.name]


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    '''Функция для сортировки вакансий по размеру зарплаты'''

    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    '''Функция для вывода заданного кол-ва вакансий с наиболее высокой зарплатой'''
    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]