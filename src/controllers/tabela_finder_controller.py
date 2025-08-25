from typing import Dict, List
from src.models.entities.tabela import Tabela
from src.models.respository.tabela_repository import tabela_repository

class TabelaFinderController:
    def find(self, tabela_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(tabela_finder_informations)
            tabela_list = self.__find_tabela(tabela_finder_informations)
            response = self.__format_response(tabela_list)
            return {
                "sucess": True,
                "message": response
            }
        except Exception as exception:
            return {
                "sucess": False,
                "error": f"{exception}" 
            }
        
    def __validate_fields(self,tabela_finder_informations: Dict):
        try:
            int(tabela_finder_informations["id"])
        except:
            raise Exception("id para achar a tabela deve ser inteiro")

    def __find_tabela(self, tabela_finder_informations: Dict) -> Tabela:
        id = tabela_finder_informations["id"]

        tabela_list = tabela_repository.find_tabela_by_id(id)
        if tabela_list:
            return tabela_list
        
        raise Exception(f"tabela não encontrada")

    def __format_response(self, tabelas: List[Tabela])-> Dict:
        response = {
            "count": 0,
            "type": "Tabela",
            "infos": []
        }
        for tabela in tabelas:
            response["infos"].append({
                    "id": tabela.id,
                    "name": tabela.name,
                    "completion": tabela.completion
            })
        return response