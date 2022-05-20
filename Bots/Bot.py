from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.caixa_comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        for index, chave in enumerate(self.caixa_comandos.comandos):
            titulo_comando = list(self.caixa_comandos.comandos[chave].keys())[0]
            print(f'{index+1} | {titulo_comando}')

    def executa_comando(self,cmd:str):
        resposta = list(self.caixa_comandos.comandos[cmd].values())[0][r.randint(0,len(self.caixa_comandos.comandos[cmd])-1)]
        return (f'Bot {self.nome} diz => {resposta}')

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass