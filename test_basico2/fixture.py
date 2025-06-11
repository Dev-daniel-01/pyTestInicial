import pytest

@pyTest.fixture

def lista_simples():
    return [1,2,3,4]


def test_somar_lista(lista_simples):
    assert sum(lista_simples) == 10
    

def test_tamanho_lista(lista_simples):
    assert len(lista_simples) == 4

def test_elementos_inteiros(lista_simples):
    assert all(isinstance(i, int) for i in lista_simples)

def test_lista_ordenada(lista_simples):
    assert lista_simples == sorted(lista_simples)


def test_lista_ordenada(lista_simples):
    assert type(lista_simples) == list
    
def test_lista_ordenada(lista_simples):
    assert max(lista_simples) == 4