from datetime import datetime


def logger(msg):
     with open("log_file.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()}: {msg}\n")


def get_log():
     with open("log_file.txt", "r", encoding="utf-8") as file:
        return file.read()


def calculator(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        pass
    