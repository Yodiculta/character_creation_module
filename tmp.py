from math import sqrt

message1: str = 'Добро пожаловать в самую лучшую программу для вычисления '
message2: str = 'квадратного корня из заданного числа'
print(message1, message2)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Выводит результат вычисления."""
    if your_number <= 0:
        return
    res: float = calculate_square_root(your_number)
    print('Мы вычислили квадратный корень из введённого вами числа. ')
    print(f'Это будет: {res}')


calc(25.5)
