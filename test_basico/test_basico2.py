from funcoes import *
    
def test_verifica_email():
    assert verifica_email("joao@gmail.com") == 'email válido'
    assert verifica_email("joao.com") == 'email incorreto'
    assert verifica_email("joao@gmail") == 'email incorreto'
    assert verifica_email("joao@outlook.com") == 'email válido'

def test_validar_senha():
    assert validar_senha("Senha123@") == 'senha cadastrada'
    assert validar_senha("senha123") == 'Erro ao cadastrar senha'
    assert validar_senha("SENHA@123") == 'senha cadastrada'
    assert validar_senha("Senha@") == 'Erro ao cadastrar senha'

def test_tamanho_string():
    assert tamanho_string("João") == 4
    assert tamanho_string("") == 0
    assert tamanho_string("Ana Maria") == 9

def test_calcular_media():
    assert calcular_media([10, 5, 5]) == 6.666666666666667
    assert calcular_media([7, 7, 7, 7]) == 7.0
    assert calcular_media([]) == 0

def test_verificar_maior_idade():
    assert verificar_maior_idade(18) == True
    assert verificar_maior_idade(17) == True
    assert verificar_maior_idade(19) == False

def test_eh_positivo():
    assert eh_positivo(5) == 'positivo'
    assert eh_positivo(0) == 'positivo'
    assert eh_positivo(-1) == 'negativo'

def test_status_aluno():
    assert status_aluno(2.5) == 'reprovado'
    assert status_aluno(5.0) == 'recuperação'
    assert status_aluno(7.5) == 'aprovado'
    assert status_aluno(3.0) == 'recuperação'
