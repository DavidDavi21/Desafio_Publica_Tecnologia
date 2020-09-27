from peewee import *
import os

arquivo = "bd_do_servidor.db"
db = SqliteDatabase(arquivo)

class BaseModel(Model):
    class Meta:
        database = db

class Partida(BaseModel):
    num_jogos = IntegerField()
    placar = IntegerField()
    min_temporada = IntegerField()
    max_temporada = IntegerField()
    quebra_recorde_min = IntegerField()
    quebra_recorde_max = IntegerField()

    def retornar():
        return "numero de jogos: " + num_jogos

if __name__ == "__main__":

	if os.path.exists(arquivo):
		os.remove(arquivo)
	db.connect()
	db.create_tables([Partida])
print(Partida.retornar())
