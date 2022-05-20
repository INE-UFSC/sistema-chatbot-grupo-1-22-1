#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotTriste import BotTriste
from Bots.BotFeliz import BotFeliz
#adicionar mais bots

lista_bots = [BotZangado("Eduardo"), BotFeliz("Lucas"), BotTriste("Beiçola")]

sys = scb.SistemaChatBot("BotsGP1",lista_bots)
sys.inicio()
