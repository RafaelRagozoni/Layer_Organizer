from typing import Dict

class TabelaRegisterController:
    def register(self, new_tabel_informations: Dict) -> Dict:
        """
        Função principal da classe, gerencia todos os processos de registro.
        Args:
            new_tabel_informations (Dict): Todas as informações enviadas no cadastro de nova tabela.

        Returns:
            response (Dict): retorna dados formatados com info util pro front-end.
        """
        try:
            self.__validate_fields(new_tabel_informations)
            ##TODO: Enviar para models para cadastro de dados
            response = self.__format_response(new_tabel_informations)
            return {
                    "sucess": True,
                    "message": response
            }
        except Exception as exception:
            return {
                "sucess": False,
                "error": str(exception)
            }

    
    def __validate_fields(self, new_tabel_informations: Dict) -> None:
        """
        Valida os campos enviados no cadastro. 

        Args:
            param1 (int):
            new_tabel_informations (Dict): Todas as informações enviadas no cadastro de nova tabela.

        Returns:
            None: Só levanta erro caso algo dê errado.
        """
        if not isinstance(new_tabel_informations["name"], str):
            raise Exception("Campo nome da tabela incorreto")

        try:
            int(new_tabel_informations["tabela_id"])
        except:
            raise Exception("ID deve ser um número!")
        
        try:
            int(new_tabel_informations["completion"])
        except:
            raise Exception("compleção deve ser um numero")
        
    def __format_response(self, new_tabel_informations: Dict) -> Dict:
        """
        Prepara e Formata a reposta pro front-end.

        Args:
            new_tabel_informations (Dict): Todas as informações enviadas no cadastro de nova tabela.

        Returns:
            mensagem (Dict): Um dicionário contendo chave/valor de informações importantes pro front-end e a mensagem final.
        """
        return {
            "count": 1,
            "type": "Tabela",
            "atributes": new_tabel_informations
        }
        