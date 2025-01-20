import os
import csv

def search_gtins_in_csv(folder_path, gtins, output_file):
    # Create a list to store the results
    results = []

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            
            # Open the CSV file and create a CSV reader
            with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
                csvreader = csv.reader(csvfile)
                
                # Loop through each row in the CSV file
                for row in csvreader:
                    # Check if any of the GTINs are in the row
                    if any(gtin in row for gtin in gtins):
                        # Add the filename and the row to the results
                        results.append([filename] + row)
    
    # Write the results to the output CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
        csvwriter = csv.writer(outfile)
        csvwriter.writerow(["Filename", "Row Data"])
        csvwriter.writerows(results)

# Define the folder path where the CSV files are located
folder_path = 'C:\\seu\\diretorio\\com\\os\\arquivos\\csv'

# Define the list of GTINs to search for
gtins = [
    '123', '1234', '12345'
]

# Define the output file path
output_file = 'resultadoDaConsulta.csv'

# Call the function
search_gtins_in_csv(folder_path, gtins, output_file)