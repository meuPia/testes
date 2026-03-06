import pytest
from meupia_testes.plugin_testes import (
    esperar_igual, esperar_diferente, esperar_verdadeiro,
    esperar_falso, esperar_maior, esperar_menor, esperar_contem
)

def test_esperar_igual(capsys):
    assert esperar_igual(10, 10, "Dez é dez") is True
    captura = capsys.readouterr()
    assert "[TESTE_OK]" in captura.out
    assert "Dez é dez" in captura.out

    assert esperar_igual("Gato", "Cachorro") is False
    captura = capsys.readouterr()
    assert "[TESTE_FALHA]" in captura.out

def test_esperar_diferente(capsys):
    assert esperar_diferente(10, 5) is True
    assert "[TESTE_OK]" in capsys.readouterr().out

    assert esperar_diferente(7, 7) is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out

def test_esperar_verdadeiro_falso(capsys):
    assert esperar_verdadeiro(True) is True
    assert "[TESTE_OK]" in capsys.readouterr().out
    
    assert esperar_verdadeiro(False) is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out

    assert esperar_falso(False) is True
    assert "[TESTE_OK]" in capsys.readouterr().out
    
    assert esperar_falso(True) is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out

def test_esperar_maior(capsys):
    assert esperar_maior(10, 5) is True
    assert "[TESTE_OK]" in capsys.readouterr().out

    assert esperar_maior(5, 10) is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out

def test_esperar_menor(capsys):
    assert esperar_menor(3, 8) is True
    assert "[TESTE_OK]" in capsys.readouterr().out

    assert esperar_menor(8, 3) is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out

def test_esperar_contem(capsys):
    lista = [1, 2, 3, "Alice", "Nathan"]
    
    assert esperar_contem(lista, "Nathan") is True
    assert "[TESTE_OK]" in capsys.readouterr().out

    assert esperar_contem(lista, "Pedro") is False
    assert "[TESTE_FALHA]" in capsys.readouterr().out