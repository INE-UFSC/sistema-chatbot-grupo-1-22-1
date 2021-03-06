
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots= [bot for bot in lista_bots if isinstance(bot, Bot)]
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Olá, usuário! Seja muito bem-vindo ao sistema {self.__empresa}!')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('-------MENU-------')
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index+1} | {bot.nome}")
        
    def escolhe_bot(self):
        while True:
            escolha = input("Escolha seu bot: ")
            if not escolha.isdigit() or int(escolha) not in range(1,len(self.__lista_bots)+1):
                print('Não entendi sua escolha...')
                self.mostra_menu()
                continue
            else:
                self.__bot = self.__lista_bots[int(escolha)-1]
                print(f'Bot {self.__bot.nome} escolhido com sucesso!')
                break
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()
    
    def le_envia_comando(self):
        while True:
            self.mostra_comandos_bot()
            nr_comando = input(f'Escolha um comando para o Bot {self.__bot.nome} [-1 PARA SAIR]: ')
            if nr_comando == '-1':
                print(self.__bot.despedida())
                break
            elif nr_comando not in self.__bot.caixa_comandos.comandos:
                print('Este comando não existe...')
                continue
            else:
                print(self.__bot.executa_comando(nr_comando))
                continue
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot      
        self.escolhe_bot()
        ##mostra mensagens de boas-vindas do bot escolhido
        print(self.__bot.boas_vindas())
        print(self.__bot.apresentacao())
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        self.le_envia_comando()




