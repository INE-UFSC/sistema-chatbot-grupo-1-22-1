#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
#adicionar mais bots

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Eduardo"), BotTriste("Beiçola")]

sys = scb.SistemaChatBot("BotsGP1",lista_bots)
sys.inicio()
