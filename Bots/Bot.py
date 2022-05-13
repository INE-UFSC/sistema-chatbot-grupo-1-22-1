from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.comandos = {}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    def mostra_comandos(self):
        for index, comando in enumerate(comandos):
            print(f'{index+1} | {self.comandos[f'{index+1}'][0]}')

    def executa_comando(self,cmd:str):
        return self.comandos[f'{cmd}'][1]

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass