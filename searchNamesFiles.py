import os
import csv
#ESTE SCRIPT ESTÁ AJUSTADO PARA OS ARQUIVOS (CIPRE, CIART, CIINV) 
# Caminho da pasta que contém os arquivos
pasta = 'C:\\Users\\OSuper\\Desktop\\Chedraui\\SearchFIles'

# Prefixos a serem verificados nos nomes dos arquivos
# Quando for colocar numeros com menos digitos EX: 6 ou 12, colocar o 0 a esquerda EX CIPRE006 ou CIPRE012
prefixos = [
    'CIART002', 'CIINV077', 'CIPRE056', 'CIPRE999', 'CIPRE555', 'CIART555', 'Ofertas_0003', 'Ofertas_0004'
]

# Lista para armazenar os nomes dos arquivos que contêm os prefixos
arquivos_encontrados = []
prefixos_nao_encontrados = set(prefixos)

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verifica se o nome do arquivo começa com algum dos prefixos
    for prefixo in prefixos:
        if nome_arquivo.startswith(prefixo):
            # Captura os caracteres relevantes do nome do arquivo
            if nome_arquivo.startswith("Ofertas_"):
                parte_nome = nome_arquivo[8:12]
            else:
                parte_nome = nome_arquivo[5:8]
            # Adiciona a parte do nome do arquivo e o nome completo à lista
            arquivos_encontrados.append((parte_nome, nome_arquivo, 'found'))
            # Remove o prefixo da lista de não encontrados
            prefixos_nao_encontrados.discard(prefixo)
            break

# Ordena a lista de arquivos encontrados
arquivos_encontrados.sort()

# Caminho do arquivo CSV de saída
csv_saida = 'arquivos_encontradosTESTES.csv'

# Escreve os nomes dos arquivos no arquivo CSV
with open(csv_saida, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Store', 'Filename', 'Status'])  # Cabeçalho do CSV
    if arquivos_encontrados:
        for parte_nome, nome_completo, status in arquivos_encontrados:
            escritor_csv.writerow([parte_nome, nome_completo, status])
    if prefixos_nao_encontrados:
        escritor_csv.writerow(['Store', 'Filename', 'Status'])  # Cabeçalho para não encontrados
        for prefixo in sorted(prefixos_nao_encontrados):
            if prefixo.startswith("Ofertas_"):
                parte_nome = prefixo[8:12]  # Últimos 4 caracteres após "Ofertas_"
            else:
                parte_nome = prefixo[-3:]  # Últimos 3 caracteres do prefixo
            escritor_csv.writerow([parte_nome, f'{prefixo} not found', 'not found'])

print(f'Arquivo CSV "{csv_saida}" criado com sucesso!')