from src.utils import get_vacancies_by_salary, get_top_vacancies, filter_vacancies
from src.HeadHunterAPI import HeadHunterAPI
from src.JSONSaver import JSONSaver
from src.Vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    search_query = input("Введите поисковый запрос: ")

    print('Пожалуйста, подождите...')

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.load_vacancies(search_query)



    filter_word = input("Введите ключевое слово для фильтрации вакансий: ")
    if filter_word:
        filtered_list = filter_vacancies(hh_vacancies, filter_word)
    else:
        filtered_list = hh_vacancies

    try:
        salary_from = int(input("Укажите нижний порог зарплаты: "))
        if not isinstance(salary_from, (float, int)):
            salary_from = 0
    except ValueError:
        salary_from = 0
    try:
        salary_to = int(input("Укажите верхний порог зарплаты: "))
        if not isinstance(salary_to, (float, int)):
            salary_to = 100000000
    except ValueError:
        salary_to = 100000000

    filtered_salary_list = get_vacancies_by_salary(filtered_list, salary_from, salary_to)

    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        result_list = []

        if top_n > len(filtered_salary_list):
            top_n = len(filtered_salary_list) - 1
            result_list = get_top_vacancies(filtered_salary_list, top_n)
        else:
            result_list = get_top_vacancies(filtered_salary_list, top_n)
    except ValueError:
        top_n = 10
        result_list = get_top_vacancies(filtered_salary_list, top_n)

    saver = JSONSaver()

    for vacancy in result_list:
        vacancy_for_file = Vacancy(vacancy.name, vacancy.url, vacancy.requirement, vacancy.responsibility,
                                   vacancy.salary)
        saver.add_vacancy(vacancy_for_file)
        print(f'\nНаименование вакансии: {vacancy.name}\n'
              f'Ссылка на вакансию: {vacancy.url}\n'
              f'Требования: {vacancy.requirement}\n'
              f'Обязанности: {vacancy.responsibility}\n'
              f'Зарплата: {vacancy.salary}\n')
#
#
if __name__ == "__main__":
    user_interaction()

