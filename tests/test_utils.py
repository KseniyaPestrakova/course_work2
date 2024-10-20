from src.utils import get_vacancies_by_salary, filter_vacancies, sort_vacancies_by_salary, get_top_vacancies


def test_get_vacancies_by_salary(vacancies):
    # Проверка на пустой результат
    assert get_vacancies_by_salary(vacancies, 6000, 7000) == []

    # Проверка на несколько результатов
    result = get_vacancies_by_salary(vacancies, 2000, 4000)
    assert len(result) == 3
    assert [v.name for v in result] == ["Java Developer", "Python Engineer", "Data Scientist"]

    # Проверка на обработку некорректного диапазона
    assert get_vacancies_by_salary(vacancies, 5000, 1000) == []


def test_filter_vacancies(vacancies):
    # Проверка фильтрации по слову "Python"
    result = filter_vacancies(vacancies, "Python")
    assert len(result) == 2
    assert all("Python" in v.name for v in result)

    # Проверка фильтрации по слову, которого нет в названиях
    result = filter_vacancies(vacancies, "C++")
    assert len(result) == 0

    # Проверка фильтрации по пустой строке (должны вернуться все вакансии)
    result = filter_vacancies(vacancies, "")
    assert len(result) == len(vacancies)
    assert result == vacancies


def test_sort_vacancies_by_salary(vacancies):
    # Проверка правильности сортировки
    sorted_vacancies = sort_vacancies_by_salary(vacancies)
    assert [v.salary for v in sorted_vacancies] == [5000, 4000, 3000, 2000, 1000]

    # Проверка, что все вакансии сохранены после сортировки
    assert len(sorted_vacancies) == len(vacancies)


def test_get_top_vacancies(vacancies):
    # Проверка вывода топ-3 вакансий
    top_3 = get_top_vacancies(vacancies, 3)
    assert len(top_3) == 3
    assert [v.salary for v in top_3] == [5000, 4000, 3000]

    # Проверка вывода всех вакансий, если top_n больше количества вакансий
    all_vacancies = get_top_vacancies(vacancies, 10)
    assert len(all_vacancies) == 5
    assert [v.salary for v in all_vacancies] == [5000, 4000, 3000, 2000, 1000]

    # Проверка вывода пустого списка, если top_n = 0
    assert get_top_vacancies(vacancies, 0) == []
