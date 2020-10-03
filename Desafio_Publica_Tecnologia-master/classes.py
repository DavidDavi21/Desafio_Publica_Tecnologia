from peewee import *
import os

arquivo = "bd_do_servidor.db"
db = SqliteDatabase(arquivo)

class BaseModel(Model):
    class Meta:
        database = db

class Partida(BaseModel):
    num_jogos = PrimaryKeyField()
    placar = IntegerField()
    min_temporada = IntegerField()
    max_temporada = IntegerField()
    quebra_recorde_min = IntegerField()
    quebra_recorde_max = IntegerField()

    def deletar_tabela():

        db.drop_tables([Partida])
        db.create_tables([Partida])
        partidinha = Partida.create(num_jogos=0, placar=0, min_temporada=0, max_temporada=0, quebra_recorde_min=0, quebra_recorde_max=0)
        
        return True

if __name__ == "__main__":

	if os.path.exists(arquivo):
		os.remove(arquivo)
	db.connect()
	db.create_tables([Partida])
partida = Partida.select()
lista_numero_jogos = []
for percorrer in partida:
    lista_numero_jogos.append(percorrer.num_jogos)
if len(lista_numero_jogos) == 0:
    partidinha = Partida.create(num_jogos=0, placar=0, min_temporada=0, max_temporada=0, quebra_recorde_min=0, quebra_recorde_max=0)
    print("Salvou os números zeros!")
else:
    print("Deu tudo certo.")
