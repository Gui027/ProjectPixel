import requests
import csv

# Endereço da API
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

# Chamada à API
resposta = requests.get(url)

# Decodificação da resposta
dados = resposta.json()

# Criação do arquivo CSV
arquivo = open("dados.csv", "w", newline="")

# Escrita dos dados no arquivo CSV
escritor = csv.writer(arquivo)
escritor.writerow(["success", "deck_id", "remaining", "shuffled"])

# Adicionando dados ao arquivo CSV
escritor.writerow([dados["success"], dados["deck_id"], dados["remaining"], dados["shuffled"]])

# Fechamento do arquivo CSV
arquivo.close()
