from dotenv import load_dotenv
import os

load_dotenv()


class TestConfig:
    BASE_UI_URL = os.getenv('BASE_UI_URL')
    BASE_API_URL = os.getenv('BASE_API_URL')