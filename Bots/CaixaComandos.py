class CaixaComandos:
    def __init__(self, dicionario_comandos:dict):
        self.__comandos = dicionario_comandos

    @property
    def comandos(self):
        return self.__comandos
