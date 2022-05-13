from Bots.BotZangado import BotZangado

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print(f'Olá, usuário! Seja muito bem-vindo ao sistema {self.__empresa}!')
        ##mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print('-------MENU-------')
        for index, bot in enumerate(self.__lista_bots):
            print(f"{index+1} | {bot.nome}")
        
    def escolhe_bot(self):
        escolha = input("Escolha seu bot: ")
        self.__bot = self.__lista_bots[int(escolha)]
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        return self.__bot.mostra_comandos()
    

    def le_envia_comando(self):
        nr_comando = input(f'Escolha um comando para o bot {self.__bot.nome}: ')
        if nr_comando not in self.__bot
        self.__bot.executa_comando(f'{nr_comando}')
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        self.boas_vindas()
        ##mostra o menu ao usuário
        self.mostra_menu()
        ##escolha do bot      
        self.escolhe_bot()
        ##mostra mensagens de boas-vindas do bot escolhido
        self.__bot.boas_vindas()
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        while True:
            mostrar_comandos_bot()
            le_envia_comando()

        

bot1 = BotZangado('Jonata')
sistema = SistemaChatBot("ufsc", [bot1])



