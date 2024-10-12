from src.Vacancy import Vacancy


def get_vacancies_by_salary_from(vacancies: list[Vacancy], salary_from: int) -> list[Vacancy]:
    """Возвращает список вакансий в заданном диапазоне зарплат"""

    return [vac for vac in vacancies if vac.salary >= salary_from]


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортирует вакансии по зарплате"""

    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Возвращает топ N вакансий по зарплате"""
    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]