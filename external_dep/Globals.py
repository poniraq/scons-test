from typing import Any

global_dict = {}

def Export(key: str, v: any):
    global_dict[key] = v

def Import(key: str, default: Any = None) -> Any:
    if (default != None):
        return global_dict.get(key, default)
    return global_dict[key]