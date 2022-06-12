from jsonpath import jsonpath

def extractor(obj: dict, expr: str = '.'):
    try:
        result = jsonpath(obj, expr)[0]
    except Exception as e:
        result = expr
    return result