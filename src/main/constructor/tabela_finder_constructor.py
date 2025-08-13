from src.views.tabela_finder_view import TabelaFinderView

def tabela_finder_constructor():
    tabela_finder_view = TabelaFinderView()
    # instaciar o controller

    tabela_finder_informations = tabela_finder_view.find_tabela_view() 
    #mandar pra controller