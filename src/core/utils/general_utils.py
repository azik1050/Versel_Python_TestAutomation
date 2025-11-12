def to_json_index_str(key: list | str):
    if isinstance(key, str):
        return f'[{key}]'
    elif isinstance(key, list):
        return ''.join([f'[{x}]' for x in key])
