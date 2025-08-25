import os
from typing import Dict
from src.controllers.tabela_finder_controller import TabelaFinderController

class TabelaFinderView:        
    def find_tabela_view(self) -> Dict:
        os.system('cls||clear')
        
        print("Buscar Tabela")
        tabela_id = input("Qual tabela deseja acessar: ")

        tabela_finder_informations = {
            "id": tabela_id
        }
        return tabela_finder_informations
    
    def find_table_sucess(self,message:Dict) -> None:
        os.system("clas||clear")

        sucess_message = f'''
            Tabela encontrada com sucesso!
            
            Tipo: {message["type"]}
            Registros: {message["count"]}
            Infos:
        '''
        for info in message["infos"]:
            sucess_message = f'''{sucess_message}
                - {info["name"]}
            '''
        print(sucess_message)
    
    def find_table_error(self, error: str) -> None:
        os.system("clas||clear")

        fail_message = f'''
        Falha ao encontrar usuario!

        Erro: {error}
        '''
        print(fail_message)