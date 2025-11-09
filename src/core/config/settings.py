from dotenv import load_dotenv
import os

load_dotenv()


class ApiConfig:
    BASE_API_URL = os.getenv('BASE_API_URL')
    BASE_JIRA_API_URL = os.getenv('BASE_JIRA_API_URL')
    JIRA_USER = os.getenv('JIRA_USER')
    JIRA_PASSWORD = os.getenv('JIRA_PASSWORD')


class UiConfig:
    BASE_UI_URL = os.getenv('BASE_UI_URL')
    BROWSER = os.getenv('BROWSER')
    IMPLICIT_DRIVER_WAIT = int(os.getenv('IMPLICIT_DRIVER_WAIT'))


class TestConfig:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    UI = UiConfig()
    API = ApiConfig()


# class TestConfig:
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     BASE_UI_URL = os.getenv('BASE_UI_URL')
#     BASE_API_URL = os.getenv('BASE_API_URL')
#     IMPLICIT_DRIVER_WAIT = int(os.getenv('IMPLICIT_DRIVER_WAIT'))
#     BROWSER = os.getenv('BROWSER')
#     BASE_JIRA_API_URL = os.getenv('BASE_JIRA_API_URL')

