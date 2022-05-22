from abc import ABC, abstractmethod
import random as r
from Bots.CaixaComandos import CaixaComandos

class Bot(ABC):
    def __init__(self, nome: str,  dicionario_comandos: CaixaComandos):
        self.nome = nome
        self.__caixa_comandos = CaixaComandos(dicionario_comandos)

    @property
    def nome(self):
        return self.__nome

    @property
    def caixa_comandos(self):
        return self.__caixa_comandos

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        for index, chave in enumerate(self.__caixa_comandos.comandos):
            titulo_comando = list(self.__caixa_comandos.comandos[chave].keys())[0]
            print(f'{index+1} | {titulo_comando}')

    def executa_comando(self,cmd:str):
        resposta = list(self.__caixa_comandos.comandos[cmd].values())[0][r.randint(0,len(self.__caixa_comandos.comandos[cmd])-1)]
        return (f'Bot {self.nome} diz => {resposta}')

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass