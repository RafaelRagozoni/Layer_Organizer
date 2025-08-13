import os
from typing import Dict

class TabelaRegisterView:
    def registry_tabela_view(self) -> Dict:
        os.system('cls||clear')
        
        print("Buscar Tabela")
        tabela_id = input("Qual numero da tabela deseja colocar: ")
        name = input("Qual nome tabela deseja colocar: ")
        completion = input("Qual completion tabela deseja colocar: ")

        new_tabela_informations = {
            "tabela_id": tabela_id,
            "name": name,
            "completion": completion,
        }

        return new_tabela_informations