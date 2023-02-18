menu = '''Калькулятор:
1 - Вычислить выражение
2 - Просмотр лога
3 - Выход
'''


def display_menu():
    while True:
        print(menu)    
        number = input(">>> ")
        if number.isdigit():
            if int(number) in (1, 2, 3):
                return int(number)


def get_value():
    pass


def output(result):
    pass