def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multy(a: object, b: object) -> object:
    return a*b
def div(a,b):
    if b == 0:
        raise ValueError("Ошибка. Деление на ноль")
    else:
        return a / b
