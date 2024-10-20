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
