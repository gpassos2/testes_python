import requests
from datetime import datetime, date


resposta = requests.get('https://api.github.com/users/gpassos2')

print(resposta.status_code)

json = resposta.json()

url = resposta.url
nome = json['name']
login = json['login']
repositorio_publico = json['public_repos']
data_hora_criacao = json['created_at'].split('T')
data_criacao = datetime.strptime(data_hora_criacao[0],'%Y-%m-%d').date()
hora_criacao = data_hora_criacao[1].split('Z')


print(f'url : {resposta.url}')
print(f'nome : {nome}')
print(f'login : {login}')
print(f'Repositorios Publicos : {repositorio_publico}')
print(f'Data da criação : {data_criacao}')
print(f'Hora da criação : {hora_criacao[0]}')