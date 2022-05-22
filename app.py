#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
from Bots.BotSolitario_gp4 import BotSolitario
from ComandosBots.dbComandos import comandosBotTriste
#adicionar mais bots

lista_bots = [
    #BotZangado("Eduardo"), BotFeliz("Lucas"), 
    BotTriste("Beiçola", comandosBotTriste()), 
    #BotSolitario('Fernanda'),5
    ]

sys = scb.SistemaChatBot("BotsGP1",lista_bots)
sys.inicio()
