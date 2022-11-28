def get_methods_from_class(target):
    return [
            func for func in dir(target) 
            if callable(getattr(target, func)) and not func.startswith("__")
    ]