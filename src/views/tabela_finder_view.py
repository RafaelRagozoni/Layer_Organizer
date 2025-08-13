import os
from typing import Dict

class TabelaFinderView:
    def find_tabela_view(self) -> Dict:
        os.system('cls||clear')
        
        print("Buscar Tabela")
        tabela_id = input("Qual tabela deseja acessar: ")

        tabela_finder_informations = {
            "tabela_id": tabela_id
        }
        return tabela_finder_informations