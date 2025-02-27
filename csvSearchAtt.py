import os
import csv
import sys

csv.field_size_limit(sys.maxsize)

def search_terms_in_csv(folder_path, search_terms, output_file):
    # Crie uma lista para armazenar os resultados
    results = []
    total_terms_found = 0
    not_found = []
    log_entries = []

    # Loop através de todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            terms_found_in_file = 0
            terms_not_found = set(search_terms)
            terms_found = set()
            
            # Log do arquivo que está sendo processado
            print(f"Processando arquivo: {filename}")
            
            # Abra o arquivo CSV e crie um leitor de CSV pode ser mudado o encoding para 'utf-8-sig' se necessário
            # Também pode ser mudado o delimitador do csv.reader para outro caractere, por exemplo csv.reader(csvfile, delimiter=';')
            with open(file_path, mode='r', encoding='latin1') as csvfile:
                csvreader = csv.reader(csvfile, delimiter='|')
                
                # Loop através de cada linha no arquivo CSV
                for row in csvreader:
                    # Verifique se algum dos termos de busca está na linha
                    for term in search_terms:
                        if term in row:
                            # Adicione o nome do arquivo e a linha aos resultados
                            results.append([filename] + row)
                            terms_found_in_file += 1
                            terms_found.add(term)
                            if term in terms_not_found:
                                terms_not_found.remove(term)

            # Adicione os termos não encontrados à lista de não encontrados
            for term in terms_not_found:
                adjusted_filename = filename[5:8]
                not_found.append([term, adjusted_filename])
                
            # Log do arquivo processado e termos encontrados
            log_entry = {
                "filename": filename,
                "terms_found": terms_found_in_file,
                "terms_found_list": list(terms_found),
                "terms_not_found": len(terms_not_found),
                "not_found_list": list(terms_not_found)
            }
            log_entries.append(log_entry)
            total_terms_found += terms_found_in_file

            # Log do processamento do arquivo
            print(f"Arquivo processado: {filename}, termos encontrados: {terms_found_in_file}")

    # Escreva os resultados no arquivo CSV de saída
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(["Filename", "Row Data"])
        csvwriter.writerows(results)

    # Escreva os termos não encontrados no arquivo CSV de saída
    with open('termos_nao_encontrados.csv', mode='w', newline='', encoding='utf-8-sig') as not_found_file:
        csvwriter = csv.writer(not_found_file)
        csvwriter.writerow(["Term", "Filename"])
        csvwriter.writerows(not_found)

    # Escreva o log completo em um arquivo separado
    with open('log_completo.txt', mode='w', encoding='utf-8') as log_file:
        for entry in log_entries:
            log_file.write(f"Arquivo: {entry['filename']}\n")
            log_file.write(f"  Termos encontrados: {entry['terms_found']}\n")
            log_file.write(f"  Lista de termos encontrados: {entry['terms_found_list']}\n")
            log_file.write(f"  Termos não encontrados: {entry['terms_not_found']}\n")
            log_file.write(f"  Lista de termos não encontrados: {entry['not_found_list']}\n\n")

    # Log do total de termos encontrados
    if total_terms_found > 0:
        print(f"Total de termos encontrados: {total_terms_found}")
    else:
        print("Nenhum termo encontrado em nenhum arquivo")

# Defina o caminho da pasta onde os arquivos CSV estão localizados
folder_path = 'C:\\Users\\OSuper\\Desktop\\Chedraui\\ttst'

# Defina a lista de termos para procurar
# A pesquisa do precisa ser exata ou seja se tiver zeros a esquerda precisa ter na consulta
search_terms = [
    '000000000003833987','000000000003833983','000000000003833985','000000000003837993','000000000003824604','000000000003824603','000000000003824602','000000000003745661','000000000003248887', '000000000001008114', '000000000003001685', '000000000001008114', '000000000003001718'
]

# Defina o caminho do arquivo de saída
output_file = 'TESTEresultadoDaConsulta.csv'

# Chame a função
search_terms_in_csv(folder_path, search_terms, output_file)