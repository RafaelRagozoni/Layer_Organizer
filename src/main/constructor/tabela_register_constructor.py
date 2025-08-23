from typing import Dict
from src.views.tabela_register_view import TabelaRegisterView
from src.controllers.tabela_register_controller import TabelaRegisterController


class TabelaRegisterConstructor:
    def __init__(self) -> None:
        '''
        função apenas para instanciar objetos com funções
        que serão utilizadas várias vezes
        '''
        self.tabela_register_view = TabelaRegisterView()
        self.tabela_register_controller = TabelaRegisterController()

    def tabela_register_constructor(self):
        new_tabela_informations = self.tabela_register_view.registry_tabela_view() 
        response = self.tabela_register_controller.register(new_tabela_informations)
        
        # Mandar resposta pro banco
        if response["sucess"]:
            self.tabela_register_view.registry_table_sucess(response["message"])
        else:
            self.tabela_register_view.registry_table_fail(response["error"])