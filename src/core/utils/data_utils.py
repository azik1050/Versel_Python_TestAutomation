from httpx import Response


def find_json_key(json: dict, path: list):
    if len(path) == 1:
        try:
            return json[path[0]]
        except KeyError:
            raise KeyError(f"The target value does not exist")
    else:
        new_path = path[1:]
        return find_json_key(json[path[0]], new_path)


def get_json_value(key: str | list, response: Response):
    if isinstance(key, str):
        actual_value = response.json()[key]
    elif isinstance(key, list):
        actual_value = find_json_key(response.json(), key)
    else:
        raise TypeError("Key must be str or list of str")
    return actual_value