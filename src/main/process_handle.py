from .constructor.introduction_process import introduction_process


def start() -> None:
    while True:
        command = introduction_process()
        if command == "1":
            print("1 foi acionado")
        elif command == "2":
            print("2 foi acionado")
        elif command == "5":
            exit(0)
        else:
            print("comando não encortado")
