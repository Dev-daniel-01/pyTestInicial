import requests

def buscar_cep(cep):
    resposta = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    if resposta.status_code != 200:
        return 'Cep Inválido'
    else:
        cep_encontrado = resposta.json()
        return cep_encontrado
    
cep = input("informe o cep: ") 
resultado = buscar_cep(cep)

print(f'\nregiao: {resultado['regiao']}')
print(f'\nestado: {resultado['estado']}')
print(f'\nlocalidade: {resultado['localidade']}')
print(f'\nbairro: {resultado['bairro']}')
print(f'\nRua: {resultado['logradouro']}\n')
