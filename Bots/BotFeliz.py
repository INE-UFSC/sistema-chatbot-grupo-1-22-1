from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome:str):
        super().__init__(nome)
        self.comandos = {"1": ("Bom dia", "Bom dia, como está você?"), 
                         "2": ("Seu nome", f"Meu nome é {self.nome}"),
                         "3": ("Quero um conselho", "Carpe diem"),
                         "4": ("Mensagem de despedida", "Foi cedo")}

    def apresentacao(self):
        return f'Meu nome é {self.nome} e você tá muito bonito(a) hoje!'
    
    def boas_vindas(self):
        return 'Obrigado, por me escolher, me sinto honrado!'

    def despedida(self):
        return 'Foi um prazer. Tenha um belo dia!'