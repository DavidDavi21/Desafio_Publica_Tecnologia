from classes import Partida
from peewee import *

def organizar_dados(placar, partida):

    contagem_num_jogos = 0
    lista_placares =[[],[]]
    quebra_recorde_max = 0
    quebra_recorde_min = 0

    for contador in partida:

        lista_placares[0].append(contador.min_temporada)
        lista_placares[1].append(contador.max_temporada)
        segundo_contador = contador.num_jogos

        quebra_recorde_max = contador.quebra_recorde_max
        quebra_recorde_min = contador.quebra_recorde_min

    if placar > lista_placares[1][-1]:
        max_temporada = placar
        if len(lista_placares[1]) != 1:
            quebra_recorde_max += 1
    else:
        max_temporada = lista_placares[1][-1]

    if placar < lista_placares[0][-1] or segundo_contador == 0:
        min_temporada = placar
        if len(lista_placares[0]) != 1:
            quebra_recorde_min += 1
        else:
            quebra_recorde_min = 0
    else:
        min_temporada = lista_placares[0][-1]

    contagem_num_jogos += 1
    return salvar_dados_bd(contagem_num_jogos, placar, min_temporada, max_temporada, quebra_recorde_max, quebra_recorde_min, partida)

def salvar_dados_bd(contagem_num_jogos, placar, min_temporada, max_temporada, quebra_recorde_max, quebra_recorde_min, partida):
    
    for contador in range(1):
        for segundo_contador in partida:
            num_jogos = segundo_contador.num_jogos + contagem_num_jogos

    salvo = Partida.create(num_jogos=num_jogos, placar=placar, min_temporada=min_temporada, max_temporada=max_temporada, quebra_recorde_max=quebra_recorde_max, quebra_recorde_min=quebra_recorde_min)
    return True

def deletar_dados():

    deletado = Partida.deletar_tabela()

    return True