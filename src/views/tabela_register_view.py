import os
from typing import Dict

class TabelaRegisterView:
    def registry_tabela_view(self) -> Dict:
        '''
        Metódo principal da classe de visualização de registro de tabela.
        Mostra opções para o usuário e um feedback da operação.

        Args:

        Return:
            new_tabela_informations (Dict): Informações da tabela que o usuário colocou.
        '''
        os.system('cls||clear')
        
        print("Buscar Tabela")
        tabela_id = input("Qual numero da tabela deseja colocar: ")
        name = input("Qual nome tabela deseja colocar: ")
        completion = input("Qual completion tabela deseja colocar: ")

        new_tabela_informations = {
            "id": tabela_id,
            "name": name,
            "completion": completion,
        }

        return new_tabela_informations
    
    def registry_table_sucess(self, message: Dict) -> None:
        '''
        Feedback que a operação foi concluída e o que foi alterado.

        Args:
            message (Dict):
        Return:
            None (None):
        '''
        os.system('cls||clear')

        sucess_message = f"""
        Usuario cadastrado com sucesso

        Tipo: {message["type"] }
        Registros: {message["count"] }
        Infos:
            Nome: {message["atributes"]["name"]}
            Completado: {message["atributes"]["completion"]}%
        """
        print(sucess_message)

    def registry_table_fail(self, error: Exception) -> None:
        '''
        Feedback que a operação não foi concluída e qual erro.

        Args:
            error (Exception): erro que deu.
        Return:
            None (None):
        '''
        os.system('cls||clear')

        fail_message = f"""
        Usuario não cadastrado!!!!

        Motivo: { error }
        """
        print(fail_message)