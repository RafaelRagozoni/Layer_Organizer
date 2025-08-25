from src.views.tabela_finder_view import TabelaFinderView
from src.controllers.tabela_finder_controller import TabelaFinderController

class TabelaFinderConstructor():
    def __init__(self):
        self.tabela_finder_view = TabelaFinderView()
        self.tabela_finder_controller = TabelaFinderController()
    def tabela_finder(self):
        tabela_finder_informations = self.tabela_finder_view.find_tabela_view() 
        response = self.tabela_finder_controller.find(tabela_finder_informations) 
        if response["sucess"]:
            self.tabela_finder_view.find_table_sucess(response["message"])
        else:
            self.tabela_finder_view.find_table_error(response["error"])