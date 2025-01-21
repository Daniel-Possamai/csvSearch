import os
import csv
import sys

csv.field_size_limit(sys.maxsize)

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
            
            # Abra o arquivo CSV e crie um leitor de CSV pode ser mudado o encoding para 'utf-8-sig' se necessário
            #Também pode ser mudado o delimitador do csv.reader para outro caractere, por exemplo csv.reader(csvfile, delimiter=';')
            with open(file_path, mode='r', encoding='latin1') as csvfile:
                csvreader = csv.reader(csvfile, delimiter='|')
                
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
folder_path = 'C:\\Users\\OSuper\\Desktop\\ciart'

# Defina a lista de termos para procurar
search_terms = [
    '9999912352882', '9999918654584', '9999918654607', '9999918654928', '9999917500202', '9999918190211', 
    '9999918514789', '9999918515540', '9999918531151', '9999918553856', '9999918553870', 
    '9999918553917', '9999918589084', '9999918589121', '9999918589206', '9999918620312', 
    '9999918620633', '9999918620657', '9999918620671', '9999918620695', '9999918627243', 
    '9999918629261', '9999918638454', '9999918639635', '9999918639659', '9999918639697', 
    '9999918641768', '9999918642215', '9999918644110', '9999918644424', '9999918646114', 
    '9999918646169', '9999918649955', '9999918649979', '9999918649993', '9999918650012', 
    '9999918653723', '9999918654546', '885645012287', '885645017732', '8718699731847', 
    '8346740017', '8346740024', '80768095289', '843076000228', '8436538812389', 
    '8436538812778', '8436538813218', '8436538813560', '7613326004992', '7613326005036', 
    '7613326005043', '7613326005067', '7622200009084', '7622210703521', '7702003450440', 
    '7798078236720', '7506292612530', '7503045180063', '7503020427329', '7503020427343', 
    '7503020605086', '7503023312127', '7503024877472', '7501668619731', '7501135505611', 
    '7501135511001', '7501055328642', '7501055328666', '7501055328673', '7501055350223', 
    '7501055350230', '7501055350247', '7501071902956', '7501083100067', '7501006584264', 
    '7501032900397', '7501032900403', '7501032920456', '7501035043138', '7500810027028', 
    '7501005180269', '41457095072', '3760038237423', '4105120003101', '37500366003188', 
    '3045140105502', '37500366003171', '13409128442', '13409341155', '13409918104', 
    '138055651547', '9999918654560'
]

# Defina o caminho do arquivo de saída
output_file = 'resultadoDaConsulta.csv'

# Chame a função
search_terms_in_csv(folder_path, search_terms, output_file)