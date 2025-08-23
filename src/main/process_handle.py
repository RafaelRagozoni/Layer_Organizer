from .constructor.introduction_process import introduction_process
from .constructor.tabela_register_constructor import TabelaRegisterConstructor
from .constructor.tabela_finder_constructor import tabela_finder_constructor

def start() -> None:
    tabela_register = TabelaRegisterConstructor()
    while True:
        command = introduction_process()
        if command == "1":
            tabela_register.tabela_register_constructor()
        elif command == "2":
            tabela_finder_constructor()
        elif command == "5":
            exit(0)
        else:
            print("comando não encortado")
