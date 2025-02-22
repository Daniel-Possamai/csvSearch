import csv

# Função para formatar os SKUs
def format_skus(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        skus = []
        
        for row in reader:
            sku = row[0].strip()
            formatted_sku = f"'{sku.zfill(18)}'"  # Adiciona zeros à esquerda para um total de 18 caracteres e coloca entre aspas simples
            skus.append(formatted_sku)
        
        outfile.write(','.join(skus))

# Caminho do arquivo de entrada e saída
input_file = 'C:\\Users\OSuper\\PythonProjects\CsvSearch\\csvSearchUpdate\\csvSearch\\skus.csv'
output_file = 'C:\\Users\OSuper\\PythonProjects\CsvSearch\\csvSearchUpdate\\csvSearch\\skus_formatted.csv'

# Formatar os SKUs
format_skus(input_file, output_file)

print("SKUs formatados com sucesso.")