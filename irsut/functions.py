def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a: object, b) -> object:
    """

    :param a:
    :param b:
    :return:
    """
    if b == 0:
        raise ValueError
    return a / b


