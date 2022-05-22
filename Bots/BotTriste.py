from Bots.Bot import Bot
from Bots.CaixaComandos import CaixaComandos
from ComandosBots.dbComandos import comandosBotTriste

class BotTriste(Bot):

    def apresentacao(self):
        return f'O-Oi, me chamo {self.nome}. Esse parece um nome triste...?'
    
    def boas_vindas(self):
        return 'Eu... Eu agradeço por me escolher. Estava muito triste e solitario antes de você chegar.'

    def despedida(self):
        return 'No final das contas, todos se vão, não é mesmo...? Será que o problema sou eu? Até mais...'