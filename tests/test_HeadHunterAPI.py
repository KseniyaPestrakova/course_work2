from src.HeadHunterAPI import HeadHunterAPI


def test_load_vacancies_returns_list():
    keyword = "Python"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)
    assert isinstance(result, list)

def test_load_vacancies_with_no_vacancies():
    keyword = "This keyword does not exist"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)
    assert len(result) == 0


def test_load_vacancies_with_valid_data():
    keyword = "Python"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)

    for vacancy in result:
        assert isinstance(vacancy, dict)
        assert "name" in vacancy
        assert "url" in vacancy
        assert "requirement" in vacancy
        assert "responsibility" in vacancy
        assert "salary" in vacancy

def test_load_vacancies_salary():
    keyword = "Python"
    hh_api = HeadHunterAPI()
    result = hh_api.load_vacancies(keyword)

    for vacancy in result:
        salary = vacancy["salary"]
        assert isinstance(salary, int) or salary == 0