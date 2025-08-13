from src.views.tabela_register_view import TabelaRegisterView

def tabela_register_constructor():
    tabela_register_view = TabelaRegisterView()
    # instaciar o controller

    new_tabela_informations = tabela_register_view.registry_tabela_view() 
    #mandar pra controller