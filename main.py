from tabela import Tabela


class Principal:
    def __init__(self):
        self.model = Tabela("teste")
        self.actions_status = {
            "0": True,
            "1": False,
            "2": False,
            "3": False,
        }
        self.action_texts = {
            "0": "Criar Tabela",
            "1": "Criar Tabela a direita",
            "2": "Criar Tabela a Esquerda",
            "3": "Acessar Tabela atual",
        }
        self.number_actions = {
            "0": self.createLayer,
            "1": self.createLayer,
            "2": self.createLayer,
            "3": self.createLayer,
        }

    def createLayer(self):
        self.model.add_layer_ahead()
        print(self.model.layers)
        # print("called")

    def CriaTabela2(self):
        print("called")

    def presentActions(self):
        for key, value in self.actions_status.items():
            if value:
                print(self.action_texts[key])

    def makeAction(self, option):
        self.number_actions[option]()


p = Principal()
p.presentActions()
op = input("Escolha uma opção: ")
p.makeAction(op)
