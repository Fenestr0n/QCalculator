import model
import view


def run_app():
        while True:
            num = view.display_menu()
            if num == 1:
                pass
            elif num == 2:
                model.get_log()
            elif num == 3:
                model.logger("Выход из программы")
                break

