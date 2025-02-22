import os
import csv

# Caminho da pasta que contém os arquivos
pasta = 'C:\\Users\\OSuper\\Desktop\\Chedraui\\TESTFILES\\Não vieram'

# Palavras-chave a serem verificadas nos nomes dos arquivos
palavras_chave = ['CIART', 'CIINV', 'CIPRE']

# Lista para armazenar os nomes dos arquivos que contêm as palavras-chave
arquivos_encontrados = []

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verifica se o nome do arquivo contém alguma das palavras-chave
    if any(palavra in nome_arquivo for palavra in palavras_chave):
        # Captura os 4 caracteres após os primeiros 5 caracteres do nome do arquivo
        parte_nome = nome_arquivo[5:8]
        # Adiciona a parte do nome do arquivo e o nome completo à lista
        arquivos_encontrados.append((parte_nome, nome_arquivo))

# Caminho do arquivo CSV de saída
csv_saida = 'arquivos_encontrados.csv'

# Escreve os nomes dos arquivos no arquivo CSV
with open(csv_saida, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Parte do Nome do Arquivo', 'Nome Completo do Arquivo'])  # Cabeçalho do CSV
    for parte_nome, nome_completo in arquivos_encontrados:
        escritor_csv.writerow([parte_nome, nome_completo])

print(f'Arquivo CSV "{csv_saida}" criado com sucesso!')