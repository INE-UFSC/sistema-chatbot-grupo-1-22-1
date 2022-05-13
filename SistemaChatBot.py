from Bots.BotZangado import BotZangado

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        pass
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index} | {bot.nome}")
        
    
    def escolhe_bot(self):
        print("Escolha seu bot:")
        self.mostra_menu()
        escolha = input('=>')
        self.__bot = self.__lista_bots[int(escolha)]
        print(f'{self.__bot}')
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        pass

    def le_envia_comando(self):
        pass
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        pass
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot

bot1 = BotZangado('Jonata')
sistema = SistemaChatBot("ufsc", [bot1])
sistema.mostra_menu()
sistema.escolhe_bot()