# How to run tests
pytest -n auto -m smoke --alluredir=allure-results // will run smokes with allure report
pytest -n auto -m "smoke or regression" --alluredir=allure-results // will run full regression with allure report
allure serve allure-results // will generate report