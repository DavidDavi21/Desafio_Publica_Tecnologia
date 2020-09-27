from classes import Partida

def organizar_dados(placar):
    print("a")
    Partida.num_jogos += 1
    percorrer = -1
    for percorrer in Partida.min_temporada:
        percorrer += 1
    if placar < Partida.min_temporada[percorrer] or len(Partida.min_temporada) == 1:
        min_temporada = placar
    elif placar > Partida.max_temporada[percorrer]:
        max_temporada = placar
    elif placar < Partida.min_temporada[percorrer] and len(Partida.min_temporada) != 1:
        quebra_recorde_min = 1
    elif placar > Partida.max_temporada[percorrer] and len(Partida.min_temporada) != 1:
        quebra_recorde_max = 1
    else:
        return "Falha na organização dos dados!"
    print("c")
    return num_jogos, placar, min_temporada, max_temporada, quebra_recorde_max, quebra_recorde_min
