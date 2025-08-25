from src.models.entities.tabela import Tabela

class __TabelaRepository:
    def __init__(self) -> None:
        self.__tabelas = []

    def registry_tabela(self, tabela: Tabela) -> None:
        self.__tabelas.append(tabela)

    def find_tabela_by_id(self, id: int) -> Tabela:
        matches = []
        for tabela in self.__tabelas:
            if tabela.id == id:
                matches.append(tabela)
        return matches
    
tabela_repository = __TabelaRepository()