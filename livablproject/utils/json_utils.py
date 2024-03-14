import json
import re


def restructure_json(json_obj, schema):
    """
    Restructures a JSON object based on a given schema.
    """
    def apply_schema(obj, schema):
        if isinstance(obj, dict):
            return {key: apply_schema(obj.get(s_key), s_val) for key, s_val in schema.items()}
        elif isinstance(obj, list):
            return [apply_schema(item, schema) for item in obj]
        else:
            return obj

    return apply_schema(json_obj, schema)

def convert_keys_to_snake_case(json_obj):
    """
    Converts all keys in a JSON object from camelCase to snake_case.
    """
    def camel_to_snake(name):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

    def convert(obj):
        if isinstance(obj, dict):
            return {camel_to_snake(key): convert(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert(item) for item in obj]
        else:
            return obj

    return convert(json_obj)
