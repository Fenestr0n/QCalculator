import model
import view


def run_app():
        while True:
            num = view.display_menu()
            if num == 1:
                exp = view.get_value()
                model.logger(f"Введите выражение: {exp}")
                res = model.calculator(exp)
                model.logger(f"Результат: {res}")
                view.output(res)
            elif num == 2:
                print(model.get_log())
                model.logger("Просмотр лога")
            elif num == 3:
                model.logger("Выход из программы")
                break

