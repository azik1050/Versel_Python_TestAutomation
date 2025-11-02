# How to run tests
pytest -n auto -m smoke --alluredir=allure-results // will run smokes with allure report
allure serve allure-results // will generate report