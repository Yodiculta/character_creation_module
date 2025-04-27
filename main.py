from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Вычисляет нанесенный урон."""
    text = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {text} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {text} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {text} {5 + randint(-3, -1)}')
    return 'не нанес урон'


def defence(char_name: str, char_class: str) -> str:
    """Вычисляет блокировку урона."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return 'не блокировал урон'


def special(char_name: str, char_class: str) -> str:
    """Вычисляет применение спец. урона."""
    text = 'применил специальное умение'
    if char_class == 'warrior':
        return (f'{char_name} {text} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {text} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {text} «Защита {10 + 30}»')
    return 'не применил специальное умение'


def start_training(char_name: str, char_class: str) -> str:
    """выбирает команду."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,')
    print('defence — чтобы блокировать атаку противника или ')
    print('special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбирает персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        print('Введи название персонажа, за которого хочешь играть: ')
        char_class = input('Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. ')
            print('Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. ')
            print('Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.')
            print(' Черпает силы из природы, веры и духов.')
        print('Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку,')
        approve_choice = input('чтобы выбрать другого персонажа').lower()
    return char_class
