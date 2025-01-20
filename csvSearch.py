import os
import csv

def search_terms_in_csv(folder_path, search_terms, output_file):
    # Crie uma lista para armazenar os resultados
    results = []
    total_terms_found = 0

    # Loop através de todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            terms_found_in_file = 0
            
            # Log do arquivo que está sendo processado
            print(f"Processando arquivo: {filename}")
            
            # Abra o arquivo CSV e crie um leitor de CSV
            with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
                csvreader = csv.reader(csvfile)
                
                # Loop através de cada linha no arquivo CSV
                for row in csvreader:
                    # Verifique se algum dos termos de busca está na linha
                    if any(term in row for term in search_terms):
                        # Adicione o nome do arquivo e a linha aos resultados
                        results.append([filename] + row)
                        terms_found_in_file += 1

            # Log do arquivo processado e termos encontrados
            if terms_found_in_file > 0:
                print(f"Arquivo processado: {filename}, termos encontrados: {terms_found_in_file}")
            else:
                print(f"Arquivo processado: {filename}, nenhum termo encontrado")
            total_terms_found += terms_found_in_file
    
    # Escreva os resultados no arquivo CSV de saída
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(["Filename", "Row Data"])
        csvwriter.writerows(results)

    # Log do total de termos encontrados
    if total_terms_found > 0:
        print(f"Total de termos encontrados: {total_terms_found}")
    else:
        print("Nenhum termo encontrado em nenhum arquivo")

# Defina o caminho da pasta onde os arquivos CSV estão localizados
folder_path = 'C:\\seu\\diretorio\\com\\os\\arquivos\\csv'

# Defina a lista de termos para procurar
search_terms = [
    '123', '1234', '12345'
]

# Defina o caminho do arquivo de saída
output_file = 'resultadoDaConsulta.csv'

# Chame a função
search_terms_in_csv(folder_path, search_terms, output_file)