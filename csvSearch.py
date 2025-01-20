import os
import csv

def search_gtins_in_csv(folder_path, gtins, output_file):
    # Crie uma lista para armazenar os resultados
    results = []

    # Loop através de todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            
            # Abra o arquivo CSV e cria um leitor de CSV
            with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
                csvreader = csv.reader(csvfile)
                
                # Loop através de cada linha no arquivo CSV
                for row in csvreader:
                    # Verifique se algum dos GTINs está na linha
                    if any(gtin in row for gtin in gtins):
                        # Adicione o nome do arquivo e a linha aos resultados
                        results.append([filename] + row)
    
    # Escreva os resultados no arquivo CSV de saída
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(["Filename", "Row Data"])
        csvwriter.writerows(results)

# Defina o caminho da pasta onde os arquivos CSV estão localizados
folder_path = 'C:\\seu\\diretorio\\com\\os\\arquivos\\csv'

# Defina a lista de GTINs para procurar
gtins = [
    '123', '1234', '12345'
]

# Defina o caminho do arquivo de saída
output_file = 'resultadoDaConsulta.csv'

# Chame a função
search_gtins_in_csv(folder_path, gtins, output_file)