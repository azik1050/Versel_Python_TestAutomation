from faker import Faker



class BaseJSONFactory:
    faker = Faker()

    @classmethod
    def _exclude_json_values(cls, json: dict, excluded_fields: list[str]) -> dict:
        for field in excluded_fields:
            json.pop(field)

        return json


    @classmethod
    def _change_json_values(cls, json: dict, custom_values: dict) -> dict:
        for key, value in custom_values.items():
            json[key] = value

        return json
