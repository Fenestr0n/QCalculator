from datetime import datetime


def logger(msg):
     with open("log_file.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()}: {msg}\n")