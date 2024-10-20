from src.Vacancy import Vacancy


def test_vacancy_class():
    # Тест 1: Проверка создания экземпляра класса
    v1 = Vacancy("Python Developer", "http://example.com", "Python, Django", "Develop web applications", 5000)
    assert v1.name == "Python Developer"
    assert v1.url == "http://example.com"
    assert v1.requirement == "Python, Django"
    assert v1.responsibility == "Develop web applications"
    assert v1.salary == 5000



    v3 = Vacancy("Data Scientist", "http://example.com", "Python, ML", "Analyze data", "Not a number")
    assert v3.salary == 0  # Некорректный тип данных для зарплаты должен быть заменен на 0

    # Тест 3: Проверка метода __str__
    v4 = Vacancy("Frontend Developer", "http://example.com", "JavaScript, React", "Develop user interfaces", 4000)
    expected_str = "Frontend Developer (Зарплата: 4000).\nТребования: JavaScript, React.\nОбязанности: Develop user interfaces.\nСсылка на вакансию: http://example.com"
    assert str(v4) == expected_str

    # Тест 4: Проверка метода vacancies_list_to_vacancy
    vacancies_list = [
        {"name": "Job1", "url": "url1", "requirement": "req1", "responsibility": "resp1", "salary": 1000},
        {"name": "Job2", "url": "url2", "requirement": "req2", "responsibility": "resp2", "salary": 2000}
    ]
    vacancy_objects = Vacancy.vacancies_list_to_vacancy(vacancies_list)
    assert len(vacancy_objects) == 2
    assert all(isinstance(v, Vacancy) for v in vacancy_objects)
    assert vacancy_objects[0].name == "Job1"
    assert vacancy_objects[1].salary == 2000


    # Тест 6: Проверка метода to_dict
    v7 = Vacancy("Test Job", "http://test.com", "Test skills", "Test responsibilities", 5000)
    v7_dict = v7.to_dict()
    assert v7_dict == {
        "name": "Test Job",
        "url": "http://test.com",
        "requirement": "Test skills",
        "responsibility": "Test responsibilities",
        "salary": 5000
    }