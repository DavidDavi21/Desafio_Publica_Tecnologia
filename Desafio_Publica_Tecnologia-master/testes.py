from gerenciador import *

def test_organizar_dados():
    assert True == organizar_dados(12,0)

def test_salvar_dados_bd():
    assert False == salvar_dados_bd(1,12,12,12,0,0,0)

def test_deletar_dados():
    assert False == deletar_dados(0)